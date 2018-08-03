import numpy as np

def hash_1(x):
	return (x + 1) % 5

def hash_2(x):
	return (3 * x + 1) % 5

if __name__ == "__main__":

	with open("char_mat.txt", "r") as handle:
		matrix = np.array([line.split() for line in handle], dtype = int)

	num_hash_fun = 2
	signature_matrix = np.array([[np.inf] * matrix.shape[1] for i in range(num_hash_fun)])

	for i, row in enumerate(matrix):

		hash_values = [hash_1(i), hash_2(i)]
		for j, col in enumerate(row):
			if (col == 1) and (signature_matrix[0, j] > hash_values[0]):
				signature_matrix[0, j] = hash_values[0]
			if (col == 1) and (signature_matrix[1, j] > hash_values[1]):
				signature_matrix[1, j] = hash_values[1]

	
	print(signature_matrix)	
