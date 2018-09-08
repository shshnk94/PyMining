import numpy as np

class eigen:
	
	def __init__(self, matrix):

		self.matrix = matrix

		return

	def __error(self, a, b):
		return np.linalg.norm(a - b)

	def __principal_eigen(self):

		flag = True
		eigen_vector = np.random.rand(self.matrix.shape[0])
	
		while flag:
	
			current_vector = np.matmul(self.matrix, eigen_vector)
			current_vector /= np.linalg.norm(current_vector)

			if self.__error(current_vector, eigen_vector) < 0.0001:
				flag = False
		
			eigen_vector = current_vector

		eigen_value = np.matmul(eigen_vector.transpose(), np.matmul(self.matrix, eigen_vector))

		return eigen_value, eigen_vector

	def eigenpairs(self):

		eigen_matrix = []	
		eigen_values = []
	
		for i in range(np.linalg.matrix_rank(self.matrix)):

			eigen_value, eigen_vector = self.__principal_eigen()
			eigen_values.append(eigen_value)
			eigen_matrix.append(eigen_vector)
		
			self.matrix -= eigen_value * (np.outer(eigen_vector, eigen_vector.transpose()))	
	
		eigen_matrix = np.array(eigen_matrix).transpose()

		return eigen_values, eigen_matrix
