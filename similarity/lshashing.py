import math
import pdb
import numpy as np
from prime import get_prime

def hash(a, b, p, m, key):
	return ((((a * key + b) % p) % m))

def get_candidate_pairs(candidate_pairs):
	
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

def locality_sensitive_hashing(signatures, no_bands, no_rows):

	#fixing bucket length equal to the signature length	
	p = get_prime(no_bands * no_rows)
	a, b= (np.random.randint(1, p-1), np.random.randint(0, p-1))

	candidate_pairs = []
	for band in range(no_bands):

		dictionary = {}
		for key, values in signatures.items():
			hash_value = hash(a, b, p, no_bands * no_rows, sum(values[(band * no_rows) : (band * no_rows) + no_rows]))
			try:
				dictionary[hash_value].append(key)
			except KeyError:
				dictionary[hash_value] = [key]
		
		for key, similar_pairs in dictionary.items():
			if len(similar_pairs) > 1:
				candidate_pairs.append(set(similar_pairs))
	
	return get_candidate_pairs(candidate_pairs)
