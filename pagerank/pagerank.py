import numpy as np
import pdb

#Calculates the mean error between new and old distribution of the random surfer

def error(old_distrib, new_distrib):
	if np.mean(np.abs(old_distrib - new_distrib)) < 0.001:
		return True

	return False

if __name__ == "__main__":
	
	#Adjacency matrix of a web graph is read from a file

	with open("web_graph.txt", "r") as handle:
		web_graph = np.array(([[int(word) for word in line.split()] for line in handle]))
	
	#Using the adjacency matrix above, we construct a transition matrix
	#And also create a distribution for a random surfer
	
	trans_matrix = np.array([row / sum(row == 1) for row in web_graph.T]).T
	vector = np.array([1] * len(trans_matrix)) / len(trans_matrix)
	
	#Iterative update of the distribution vector is done by multiplyting with the transition matrix
	#Ended when error between the new and old vector is less than a threshold, as in error(old,new)

	flag = True	
	while flag:
		new_vector = trans_matrix @ vector
		
		if error(vector, new_vector):
			flag = False
		else:
			vector = new_vector
			
	print(vector)	
		
