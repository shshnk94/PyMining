import numpy as np
import sys

"""
class Node defines the node for each bfs_tree node. Node.data stores the node information and, Node.children and 
Node.parents contain references (pointers) to the children and the parents respectively.
"""

class Node:
	
	def __init__(self, data):

		self.data = data
		self.children = []
		self.parents = []

def breadth_first_search(graph, source, discovered):
	
	"""
	Constructs the Breadth First Search Tree for a graph but with a minor tweak. A node, even if already discovered, is added 
	if it belongs to the next level of the node under observation. This helps in couting all the available shortest path to it.
	"""

	bfs_tree = Node(source)
	discovered[source] = 1
	level_count = 0
	level = [[bfs_tree]]
	flag = True

	while flag:
		next_level = []

		for node in level[level_count]:
			for neighbor in np.where(graph[node.data] == 1)[0]:
				if (discovered[neighbor] == 0) or (len([1 for item in next_level if item.data == neighbor]) != 0):

					child = Node(neighbor)
					child.parents.append(node)
					node.children.append(child)
					next_level.append(child)

					discovered[neighbor] = 1

		if not next_level:
			flag = False
		else:	
			level.append(next_level)
			level_count += 1

	return bfs_tree

def count_shortest_path(root, path_counts):

	"""
	Counts all the available shortest paths to a node from the source/root node.
	"""
	
	if root.children:

		if not root.parents:
			path_counts[root.data] = 1
		else:
			path_counts[root.data] += sum([path_counts[parent.data] for parent in root.parents])
			
		for child in root.children:
			path_counts = count_shortest_path(child, path_counts)

	else:
		path_counts[root.data] += sum([path_counts[parent.data] for parent in root.parents])
			
	return path_counts	

def credit_calculation(root, path_counts, credit_matrix):
	
	"""
	Calculates credits or betweenness measure for each edge of a bfs_tree recursively. Credit of each node is the
	sum of the credits of the edges from the node to the nodes in the next level. Thus calculated credit is divided 
	"proportionately" among the edges to the node from it's parents.
	"""

	if not root.children:

		#For all nodes (other than leaf), node credit is calculated by adding the credits of the edges to next level.
		for parent in root.parents:
			credit_matrix[parent.data, root.data] += path_counts[parent.data] / path_counts[root.data]
			credit_matrix[root.data, parent.data] = credit_matrix[parent.data, root.data]

	else:	
		credit = 1
		for child in root.children:
			credit_matrix = credit_calculation(child, path_counts, credit_matrix)
			credit += credit_matrix[root.data, child.data]
		
		#For all nodes (other than root), divided credit proportionately as mentioned above.
		if root.parents:
			for parent in root.parents:
				credit_matrix[parent.data, root.data] += (path_counts[parent.data] / path_counts[root.data]) * credit
				credit_matrix[root.data, parent.data] = credit_matrix[parent.data, root.data] 

	return credit_matrix			

def clustering(graph, betweenness_matrix, num_clusters):
	
	"""
	Clustering the graph nodes into required number of clusters by deleting edges with max betweenness iteratively
	"""
	
	flag = True
	
	while flag:
		
		i, j = np.unravel_index(np.argmax(betweenness_matrix), betweenness_matrix.shape)

		#deleting edge with max betweenness
		graph[i, j] = graph[j, i] = 0
		betweenness_matrix[i, j] = betweenness_matrix[j, i] = 0

		#End the clustering process when number of connected components are equal to num_clusters
		component_count = 0
		discovered = np.zeros(graph.shape[0])

		while 0 in discovered:
			breadth_first_search(graph, np.where(discovered == 0)[0][0], discovered)
			component_count += 1
			
		if component_count == num_clusters:
			flag = False

	return graph
	
if __name__ == "__main__":
	
	graph = []
	with open("graph", "r") as handle:
		for line in handle:
			graph.append(line.split())

	graph = np.array(graph, dtype = int)

	"""	
	Define a betweenness matrix, which is basically an adjacent matrix of graph with it's node weights	
	representing the betweenness measure of the edges
	"""

	betweenness_matrix = np.zeros(graph.shape)
	
	#Iterate across each node and calculate the betweenness
	for node in range(graph.shape[0]):	
		bfs_tree = breadth_first_search(graph, node, np.zeros(graph.shape[0]))
		
		path_counts = np.zeros(graph.shape[0])
		path_counts = count_shortest_path(bfs_tree, path_counts)

		credit_matrix = np.zeros(graph.shape)
		credit_matrix = credit_calculation(bfs_tree, path_counts, credit_matrix)

		betweenness_matrix += credit_matrix
	
	#Betweenness of an edge is calculated twice considering each of it's end points. Hence, divide by 2.	
	betweenness_matrix = betweenness_matrix / 2

	#print(betweenness_matrix)
	print("Enter the number of clusters required")
	num_clusters = int(sys.stdin.readline())

	cluster = clustering(graph, betweenness_matrix, num_clusters)
	print(cluster)
	
