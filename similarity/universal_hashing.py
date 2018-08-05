import sys
import math
import numpy as np
from random import randint

#get_prime(number) returns the smallest prime greater than or equal to the hash table size
def get_prime(number):	
	
	flag = True
	num = number

	while flag and num < 100:

		i = 2
		while (i <= math.sqrt(num)) and (num % i != 0):
			i += 1

		if i > math.sqrt(num):
			flag = False
		else:
			num += 1

	return num

#vector_length(max, m) calculates the maximum number of digits required to represent the universe of keys in base-m
def vector_length(maximum, base):
	r = 0
	
	while maximum != 0:
		maximum = int(maximum / base)
		r += 1

	return r

#vector(k, r, m) converts the key into vector of digits in base-m
def vector(key, r, m):
	key_vector = []

	while key != 0:
		key_vector.append(key % m)
		key = int(key / m)

	for i in range(r - len(key_vector)):
		key_vector.append(0)

	return key_vector
		

def hash(key, a, m):
	return sum([i * j for i, j in zip(key, a)]) % m
		
if __name__ == "__main__":

	print("Key universe size")	
	N = int(sys.stdin.readline())

	print("Hash table size")
	m = get_prime(int(sys.stdin.readline()))

	r = vector_length(N, m)

	print("Number of hash table elements")
	num_elements = int(sys.stdin.readline())

	#Different hash parameters (a) distinguish between the hash functions from the hash family
	hash_param = [vector(randint(0, N - 1), r, m) for i in range(num_elements)]
	
	hash_table = [[] for i in range(m)]
	for count in range(num_elements):
		key = randint(0, N - 1)
		hash_table[hash(vector(key, r, m), hash_param[count], m)].append(key)

	print(hash_table)
	
	
