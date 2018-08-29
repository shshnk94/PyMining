import numpy as np
import sys
import pdb

def merge_buckets(bucket_list):
	"""
	Merges buckets when there are more than 2 buckets of the same size. This is done recursively until no further
	merging is required.
	"""

	flag = True
	index = len(bucket_list) - 1

	while flag and (index != 1):
		
		#Check if there are 3 buckets of same size and merge the least recent two into a single bucket, adding the sizes of each.
		if bucket_list[index][1] == bucket_list[index - 1][1] == bucket_list[index - 2][1]:
			bucket_list[index - 1][1] += bucket_list[index - 2][1]
			bucket_list.pop(index - 2)
			index -= 2

		else:
			flag = False
	
	return

def motvani(bit, bucket_list, timestamp):
	"""
	Major code of Datar-Gionis-Indyk-Motwani algorithm.
	"""

	#Create the first bucket in the stream with size 1
	if not bucket_list:
		if bit == 1:
			bucket_list.append([timestamp, 1])
	
	else:

		#Removes the least recent bucket, if timestamp (of course, mod window_size) is equal to the bucket's timestamp
		if timestamp == bucket_list[0][0]:
			bucket_list.pop(0)
		
		#When a 1 is observed we add a new bucket of size 1 and merge buckets recursively if required.
		if bit == 1:
			bucket_list.append([timestamp, 1])
			merge_buckets(bucket_list)
	
	return
		
def estimate(bucket_list, k, timestamp, window_size):

	ones = 0
	index = len(bucket_list) - 1

	while (index >= 0) and ((timestamp - k + 1) >= bucket_list[index][0]):
		ones += bucket_list[index][1]
		index -= 1

	while (index >= 0) and ((timestamp - k + 1) < bucket_list[index][0]):
		ones += bucket_list[index][1]
		index -= 1

	return ones

if __name__ == "__main__":

	print("Required window size")
	window_size = int(sys.stdin.readline())

	print("Binary stream size")
	stream_size = int(sys.stdin.readline())
	
	stream = []
	timestamp = 0
	bucket_list = []

	while timestamp < stream_size:
		bit = np.random.randint(2)

		#We append the new bit into a list which is used to calculate actual count of 1's.
		stream.append(bit)
		motvani(bit, bucket_list, timestamp % window_size)

		timestamp += 1
	
	print("Number of most recent bits to be checked")
	k = int(sys.stdin.readline())

	print("Actual number of ones:", np.sum((np.array(stream) == 1)[stream_size - k:]))	
	print("Estimated number:", estimate(bucket_list, k, timestamp, window_size))
