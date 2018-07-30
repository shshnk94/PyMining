import numpy as np
import pdb

def error(old_distrib, new_distrib):
	if np.mean(np.abs(old_distrib - new_distrib)) < 0.001:
		return True

	return False

if __name__ == "__main__":
	with open("web_graph.txt", "r") as handle:
		web_graph = np.array(([[int(word) for word in line.split()] for line in handle]))
	
	trans_matrix = np.array([row / sum(row == 1) for row in web_graph.T]).T
	vector = np.array([1] * len(trans_matrix)) / len(trans_matrix)

	flag = True	
	while flag:
		new_vector = trans_matrix @ vector
		
		if error(vector, new_vector):
			flag = False
		else:
			vector = new_vector
			
	print(vector)	
		
