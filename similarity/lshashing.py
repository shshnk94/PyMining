import math
import pdb
import numpy as np

def get_prime(number):	
	
	flag = True
	num = number + 1

	while flag and num < 100:

		i = 2
		while (i <= math.sqrt(num)) and (num % i != 0):
			i += 1

		if i > math.sqrt(num):
			flag = False
		else:
			num += 1

	return num

def hash(a, b, p, m, key):
	return ((((a * key + b) % p) % m))

def get_candidate_pairs(candidate_pairs):
	#pdb.set_trace()
	pairs = 0
	while pairs < len(candidate_pairs):
		row = pairs + 1
		while row < len(candidate_pairs):
			if candidate_pairs[pairs].intersection(candidate_pairs[row]):
				candidate_pairs[pairs] = candidate_pairs[pairs].union(candidate_pairs[row])
				del candidate_pairs[row]
			else:
				row += 1
		
		pairs += 1

	return candidate_pairs

def locality_sensitive_hashing(signatures, b,  r):
	
	#fixing bucket length equal to the signature length	
	p = get_prime(b * r)
	a, b= (np.random.randint(1, p-1), np.random.randint(0, p-1))

	candidate_pairs = []
	for band in range(b):

		dictionary = {}
		for key, values in signatures.items():
			hash_value = hash(a, b, p, b * r, sum(values[(band * r) : (band * r) + r]))
			try:
				dictionary[hash_value].append(key)
			except KeyError:
				dictionary[hash_value] = [key]
		
		for key, similar_pairs in dictionary.items():
			if len(similar_pairs) > 1:
				candidate_pairs.append(set(similar_pairs))
	
	return get_candidate_pairs(candidate_pairs)
