import numpy as np
import math
import pdb

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

'''
For any 'a' in the range of 1 to p-1 inclusive and 'b' in the range of 0 to p-1 inclusive we define 
a universal family of hash functions where each function is parameterized with different values of 'a' and 'b'.

Each hash function of this family is given by,
	h(k, a, b) = ((ax + b) mod p) mod m)
where 'p' is a prime next to the maximum value in the universe of valid keys.

'''

def hash(a, b, p, m, key):
	return ((a * key + b) % p) % m

if __name__ == "__main__":

	with open("char_mat.txt", "r") as handle:
		matrix = np.array([line.split() for line in handle], dtype = int)

	num_hash_fun = 2
	p = get_prime(matrix.shape[0])
	hash_parameters = [[np.random.randint(1, p-1), np.random.randint(0, p-1)] for i in range(num_hash_fun)]
	signature_matrix = np.array([[np.inf] * matrix.shape[1] for i in range(num_hash_fun)])

	for i, row in enumerate(matrix):
		hash_values = [hash(a, b, p, matrix.shape[0], i) for a, b in hash_parameters]

		#FIXME : Collision in hash value since small p and m`	
		for j, col in enumerate(row):
			for k in range(num_hash_fun):
				if (col == 1) and (signature_matrix[k, j] > hash_values[k]):
					signature_matrix[k, j] = hash_values[k]

	print(signature_matrix)	
