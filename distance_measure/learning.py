import pandas as pd
import numpy as np
import knn
from sklearn.neighbors import KNeighborsClassifier

def split(df):

	row_index = np.random.choice(df.shape[0], int(0.7 * df.shape[0]), replace = False)	
	train = np.array(df.loc[row_index, ])
		
	test = np.array(df.loc[[i for i in range(df.shape[0]) if i not in row_index], ])

	return (train, test)

def error(test, prediction):
	return (np.sum(np.not_equal(test, prediction)) / test.shape[0])
	
	
if __name__ == "__main__":
	
	url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
	column_names = ["sepLength", "sepWidth", "petLength", "petWidth", "class"]
	train, test = split(pd.read_csv(url, header = None, names = column_names))
	
	model = knn.knn(3)
	prediction = model.predict(train, test)
	
	print("Error in custom algorithm" + " " + str(error(test[:,-1], prediction)))

	#validation of the above code using KNeighborsClassifier in sklearn
	
	model = KNeighborsClassifier(n_neighbors = 3,  algorithm = "brute", weights = "uniform")
	model.fit(train[:, :-1], train[:, -1])
	prediction = model.predict(test[:, :-1])
	
	print("Error in KNN from sklearn" + " " + str(error(test[:,-1], prediction)))
