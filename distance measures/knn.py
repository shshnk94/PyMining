import numpy as np

class knn:
	
	def __init__(self, k):
		self.k = k
	
	def distance(self, x, y):
		return np.linalg.norm(x[:-1] - y[:-1])

	def predict(self, train, test):
		
		prediction = []	
		for query in test:
			
			distances = []
			for index, point in enumerate(train):
				distances.append([index, self.distance(query, point)])
			
			distances = np.array(distances)
			nearest = distances[distances[:, 1].argsort()][0 : self.k]
			
			votes = np.array(np.unique(train[nearest[:, 0].astype(int)][:, -1], return_counts = True)).T
			prediction.append(votes[votes[:, 1].argsort()[-1], 0])

		return np.array(prediction)
