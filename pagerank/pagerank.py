import numpy as np

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
	
	trans_matrix = np.array([row / sum(row == 1) if sum(row == 1) != 0 else row for row in web_graph.T]).T
	vector = np.array([1] * len(trans_matrix)) / len(trans_matrix)
	
	#Iterative update of the distribution vector is done by multiplyting with the transition matrix
	#Ended when error between the new and old vector is less than a threshold, as in error(old,new)

	flag = True	
	beta = 0.85

	while flag:
		
		#Adds a fraction of probability that a random surfer can "teleport" into a random page
		#Eventhough the spider trap gets a large amount of Pagerank, the effect has been limited.

		new_vector = beta * (trans_matrix @ vector) + ((1 - beta) / len(trans_matrix)) * np.ones(len(trans_matrix))
		
		if error(vector, new_vector):
			flag = False
		else:
			vector = new_vector
			
	print(vector)	
		
