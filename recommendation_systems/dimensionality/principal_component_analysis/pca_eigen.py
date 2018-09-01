import numpy as np

def error(a, b):
	return np.linalg.norm(a - b)

def principal_eigen(matrix):

	flag = True
	eigen_vector = np.random.rand(matrix.shape[0])
	
	while flag:
	
		current_vector = np.matmul(matrix, eigen_vector)
		current_vector /= np.linalg.norm(current_vector)

		if error(current_vector, eigen_vector) < 0.0001:
			flag = False
		
		eigen_vector = current_vector

	eigen_value = np.matmul(eigen_vector.transpose(), np.matmul(matrix, eigen_vector))

	return eigen_value, eigen_vector
			

def eigenpairs(matrix):

	eigen_matrix = []	
	eigen_values = []
	
	for i in range(matrix.shape[0]):

		eigen_value, eigen_vector = principal_eigen(matrix)
		eigen_values.append(eigen_value)
		eigen_matrix.append(eigen_vector)
		
		matrix = matrix - eigen_value * (np.outer(eigen_vector, eigen_vector.transpose()))	
	
	eigen_matrix = np.array(eigen_matrix).transpose()

	return eigen_values, eigen_matrix
		
if __name__ == "__main__":
		
	with open("matrix", "r") as handle:
		matrix = np.array([line.split() for line in handle], dtype = float)

	symmetric_matrix = np.matmul(matrix.transpose(), matrix)

	eigen_values, eigen_matrix = eigenpairs(symmetric_matrix.copy())
	transformed_matrix = np.matmul(matrix, eigen_matrix)

	print(transformed_matrix)
