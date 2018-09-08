import numpy as np
from eigen import eigen

if __name__ == "__main__":
		
	with open("matrix", "r") as handle:
		matrix = np.array([line.split() for line in handle], dtype = float)

	symmetric_matrix = np.matmul(matrix.transpose(), matrix)

	eigen_values, eigen_matrix = eigen(symmetric_matrix).eigenpairs()	
	transformed_matrix = np.matmul(matrix, eigen_matrix)

	print(transformed_matrix)
