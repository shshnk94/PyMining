import numpy as np
import sys

def hash(a, b, m, key):
	return (((a * key + b) % m))

if __name__ == "__main__":
	
	print("Bloom filter size :")
	filter_size = int(sys.stdin.readline())
	bloom_filter = np.zeros(filter_size)

	print("Number of key values :")
	num_values = int(sys.stdin.readline())

	print("Number of hash functions :")
	num_hash_functions = int(sys.stdin.readline())

	print("Stream size")
	stream_size = int(sys.stdin.readline())
	
	hash_parameters = [[np.random.randint(0, filter_size), np.random.randint(0, filter_size)] for i in range(num_hash_functions)]

	#Initialising the bloom filter by setting the bits for the required key (in the inclusive range of 0 to 100) values
	stored_values = []
	for i in range(num_values):
		
		key = np.random.randint(0, 101)
		stored_values.append(key)

		#Hash the key across 'k' hash functions and set the bit to 1. Equivalent to cascaded bloom filters.
		for [a, b] in hash_parameters:
			bloom_filter[hash(a, b, filter_size, key)] = 1

	#Check if the key exists in the filters when a stream of those keys (100, in this case) arrive.
	allowed = []
	disallowed = []

	for i in range(stream_size):

		key = np.random.randint(0, 101)
		
		i = 0
		while i < len(hash_parameters):
			[a, b] = hash_parameters[i]
			
			if bloom_filter[hash(a, b, filter_size, key)] == 0:
				disallowed.append(key)
				break
			
			i += 1

		if i == len(hash_parameters):
			allowed.append(key)
			
	print("Stored keys")
	print(stored_values)
	
	print("Allowed keys")
	print(allowed)
	
	print("Disallowed keys")
	print(disallowed)
