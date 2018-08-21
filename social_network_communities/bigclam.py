import numpy as np
from math import exp
import pdb

def read_network():
	"""
	Reads the adjacency matrix of a network (basically a graph) from a file and
	returns it as a numpy 2D array for further convenience
	"""
	
	network = []	

	with open("network", "r") as handle:
		for line in handle:
			network.append(line.split())
	
	return np.array(network, dtype = int)

def gradient(network, strength_matrix, node, sum_all_nodes):

	sum_exponent = np.zeros(strength_matrix.shape[1])
	sum_neighbor = np.zeros(strength_matrix.shape[1])

	for neighbor in strength_matrix[np.where(network[node] == 1)]:
		
		sum_neighbor += neighbor
		exponent = exp(-np.dot(strength_matrix[node], neighbor))
		sum_exponent += (neighbor * exponent / (1 - exponent))

	return (sum_exponent - sum_all_nodes + strength_matrix[node] + sum_neighbor)
		
def optimisation(network, num_comm):
	
	strength_matrix = np.random.rand(network.shape[0], num_comm)

	#'outer' and 'inner' are two flags for the two optimisation loops as indicated by the names
	outer = True
	
	while outer:
		old_matrix = strength_matrix.copy()	

		for index, u in enumerate(strength_matrix):
			inner = True
			sum_all_nodes = np.sum(strength_matrix, axis = 0)
	
			while inner:
				strength_values = strength_matrix[index].copy()
				strength_matrix[index] += (0.01 *  gradient(network, strength_matrix, index, sum_all_nodes))
				
				if np.mean(abs(strength_values - strength_matrix[index])) < 0.01:
					inner = False
		
		if np.mean(abs(old_matrix - strength_matrix)) < 0.01:
			outer = False

	return strength_matrix

if __name__ == "__main__":
	
	network = read_network()
	print(optimisation(network, 2))
	
