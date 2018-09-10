import numpy as np

def decomposition(matrix):

	total_weight = np.linalg.norm(matrix) ** 2	

	#Obtaining the column matrix 'C' with dimension (m x r)
	population = [i for i in range(matrix.shape[1])]
	weights = [np.linalg.norm(matrix[:, i]) ** 2 / total_weight for i in range(matrix.shape[1])]	

	column_index = np.random.choice(population, 2, replace = True, p = weights)
	C = matrix[:, column_index] / np.sqrt(2 * np.array([weights[i] for i in column_index]))
	
	
	#Obtaining the row matrix 'R' with dimension (r x n)
	population = [i for i in range(matrix.shape[0])]
	weights = [np.linalg.norm(matrix[i]) ** 2 / total_weight for i in range(matrix.shape[0])]	

	row_index = np.random.choice(population, 2, replace = True, p = weights)
	R = (matrix[row_index].transpose() / np.sqrt(2 * np.array([weights[i] for i in row_index]))).transpose()

	#Obtaining the matrix 'U' with dimension (r x r)
	W = matrix[row_index][:, column_index]
	X, sigma, Y_trans = np.linalg.svd(W)

	#Moore-Penrose Pseudoinverse
	sigma_plus = np.diag(sigma)
	sigma_plus[np.where(sigma_plus != 0)] = 1 / sigma_plus[np.where(sigma_plus != 0)]

	U = np.matmul(Y_trans.transpose(), np.matmul(sigma_plus ** 2, X.transpose()))
	
	return C, U, R

if __name__ == "__main__":
		
	with open("matrix", "r") as handle:
		matrix = np.array([line.split() for line in handle], dtype = float)

	print(matrix)	
	C, U, R = decomposition(matrix)
	print(np.matmul(C, np.matmul(U, R)))
