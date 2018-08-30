import numpy as np
import numpy.ma as ma

def normalise(matrix):
	"""
	Normalises the user rating matrix by subtracting average of his ratings from his ratigs. 
	And, then subtracting the average rating of an item from it's ratings.
	"""

	#Normalise user ratings
	matrix = (matrix.transpose() - np.mean(matrix, axis = 1)).transpose()
	
	#Normalise the quality of the item
	matrix = matrix - np.mean(matrix, axis = 0)

	return matrix

def initialise(matrix, d):
	"""
	Create and initialise 'u' and 'v' matrices. To start with, we initialise each cell of these
	matrix as sqrt(mean(matrix) / dimension) so that the product of u and has the same mean as 'matrix'.
	"""
	
	initial_value = (np.mean(matrix) / d) ** 0.5

	#create 'u' of dimension (matrix.shape[0] x d)
	u = np.full((matrix.shape[0], d), initial_value)

	#create 'v' of dimension (d x matrix.shape[1])
	v = np.full((d, matrix.shape[1]), initial_value)

	return (u, v)

def error(matrix, product):
	"""
	Calculates the sum of the squared differences between 'matrix' and product of u and v.
	Minimising this quantity is same as minimising RMSE.
	"""

	return np.sum((matrix - product) ** 2)

def optimisation(matrix, u, v, d):
	"""
	Minimises the RMSE of the product of u and v by using Gradient Descent optimisation.
	The gradient equation and the variable naming is as per "UV-Decomposition" in the textbook.
	"""

	flag = True
	rmse = float('Inf')
	
	while flag:	

		#optimising each element of 'u'
		for r in range(u.shape[0]):
			for s in range(u.shape[1]):
				dot_product = [np.sum([u[r, k] * v[k, j] for k in range(d) if k != s]) for j in range(v.shape[1])]
				u[r, s] = ma.dot(v[s], matrix[r] - dot_product) / np.sum(v[s, ~np.isnan(matrix[r])] ** 2)

		#optimising each element of 'v'
		for r in range(v.shape[0]):
			for s in range(v.shape[1]):
				dot_product = [np.sum([u[i, k] * v[k, s] for k in range(d) if k != r]) for i in range(u.shape[0])]
				v[r, s] = ma.dot(u[:,r], matrix[:, s] - dot_product) / np.sum(u[~np.isnan(matrix[:, s]), r] ** 2)

		current_rmse = error(matrix, np.matmul(u, v))
		
		if current_rmse < rmse:
			rmse = current_rmse
		else:
			flag = False

			
	return

if __name__ == "__main__":
	
	matrix = []	
	with open("matrix", "r") as handle:
		for line in handle:
			matrix.append(line.split())

	matrix = np.array(matrix, dtype = float)
	
	#Replace the unrated cells with Nan (which represents the absence of ratings better).
	#Also, create a masked array for convenience of further calculations.
	matrix[matrix == 0] = np.nan
	matrix = ma.array(matrix, mask = np.isnan(matrix))

	#Normalise the matrix before further calculations.	
	normalise(matrix)

	#Create and initialise u and v matrices (both long and thin).
	dimension = 2
	u, v = initialise(matrix, dimension)

	#Optimise the value of u and v.
	optimisation(matrix,u, v, dimension)

	print(np.matmul(u, v))


