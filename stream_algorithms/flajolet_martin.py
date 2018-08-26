import numpy as np
import sys
	
def hash(a, b, m, key):
	return ((a * key + b) % m)

def trailing_zeroes(hash_value):

	binary = bin(hash_value)[2:]
	
	return (len(binary) - len(binary.rstrip('0')))

def estimate(estimate_uniques, m):

	split_size = np.ceil(np.log2(m))
	splits = np.array_split(estimate_uniques, int(len(estimate_uniques) / split_size))
	
	#Return the median value of the means of each group/split
	return np.median([np.mean(i) for i in splits])

if __name__ == "__main__":
	
	#Though stream is something dynamic, for our convenience we assume a static version here	
	print("Required stream size")
	stream_size = int(sys.stdin.readline())

	#Let's generate a "stream" of random numbers between 0 and some value inclusive
	print("Maximum value of any distinct element")
	stream = np.random.randint(0, int(sys.stdin.readline()), size = stream_size)

	#Count the actual distinct elements in the stream for further verification
	actual_uniques = len(np.unique(stream))
	
	print("Number of hash functions")
	num_hash_functions = int(sys.stdin.readline())
	hash_parameters = [[np.random.randint(1, actual_uniques), np.random.randint(1, actual_uniques)] for i in range(num_hash_functions)]

	#Flajolet-Martin Algorithm
	estimate_uniques = []

	for [a, b] in hash_parameters:
		max_trailing_zeroes = 0
		
		for element in stream:

			#Here I'm abusing my knowledge about the length of the stream, which is unknown in practical applications 
			#Hence, the size of the hash table is kept sufficiently large based on the context.
			num_trailing_zeroes = trailing_zeroes(hash(a, b, actual_uniques + 1, element))

			if num_trailing_zeroes > max_trailing_zeroes:
				max_trailing_zeroes = num_trailing_zeroes

		estimate_uniques.append(2 ** max_trailing_zeroes)

	#Another abuse of the known value. Ideally each group should some small multiple of log2(actual_uniques).
	print("Estimated number of distinct elements",estimate(np.array(estimate_uniques), actual_uniques))
	print("Actual number of distinct elements", actual_uniques)
