from threading import Thread
import glob
import queue
import pdb

def map(dict_queue, filename):
	special_chars = ".,!?;:-"
	kv_pairs = []

	with open(filename, "r") as handle:
		for line in handle:
			for word in line.split():
				kv_pairs.append((word.strip(special_chars), 1))
	
	dict_queue.put(kv_pairs)

	return

def group(dict_queue):
	dictionary = {}
	
	while not dict_queue.empty():
		kv_pairs = dict_queue.get()
		
		for key, value in kv_pairs:
			if key not in dictionary:
				dictionary[key] = [value]
			else:
				dictionary[key].append(value)

	return dictionary

def reduce(kl_pairs):
	dictionary = {}
	
	for key, values in kl_pairs.items():
		dictionary[key] = sum(values)	

	return dictionary	

if __name__ == "__main__":

	threads = []
	dict_queue = queue.Queue()
	
	for index, doc in enumerate(glob.glob("./*.txt")):
		threads.append(Thread(target = map, args = (dict_queue, doc)))
		threads[index].start()
		threads[index].join()

	dictionary = reduce(group(dict_queue))

	for key, value in dictionary.items():
		print(key + " " + str(value))

