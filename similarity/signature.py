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

def hash(a, b, p, m, keys):
	return dict(zip(keys, (((a * np.array(keys) + b) % p) % m)))

def get_list(shingles):
	item_list = []

	for key, values in shingles.items():
		item_list += values
	
	return sorted(list(set(item_list)))

def signature(shingles, m, sign_length):

	p = get_prime(m)
	hash_parameters = [[np.random.randint(1, p-1), np.random.randint(0, p-1)] for i in range(sign_length)]
	signatures = {key : [[np.inf] for count in range(len(hash_parameters))] for key in shingles}
	list_of_items = get_list(shingles)	
	
	for index, [a, b] in enumerate(hash_parameters):
		for row, hash_value in hash(a, b, p, m, list_of_items).items():
			for key, k_shingles in shingles.items():
				if (row in k_shingles) and (hash_value < signatures[key][index]):
					signatures[key][index] = hash_value

	return signatures

'''
if __name__ == "__main__":
	shingles = {"s1" : [0, 3],
				"s2" : [2],
				"s3" : [1, 3, 4],
				"s4" : [0, 2, 3]}

	print(signature(shingles, 5, 2))
'''
