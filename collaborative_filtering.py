import numpy as np
from numpy.linalg import norm
import sys
import pdb

def generate_data(num_movies, num_users):
	"""
	Creates a dummy dataset with the required number of users and movies
	"""

	data = []	
	for user in range(num_users):
		data.append([np.random.randint(0, 6) for movie in range(num_movies)])

	data = np.array(data)

	return data
	
def normalise(data):
	"""
	Users may be strict or lenient while rating. So, we normalise their rating by subtracting
	average user rating from the given ratings of a user.
	"""
	
	for user in range(data.shape[0]):
		data[user, ~np.isnan(data[user])] -= np.nanmean(data[user])
	
	return

def nannorm(vector):
	"""
	Calculates norm of a vector ignoring all the Nans.
	"""

	return norm(vector[~np.isnan(vector)])

def cosine(a, b):
	"""
	Calculates the cosine distance between 2 vectors 'a' and 'b'
	"""
	
	return np.nansum(a * b) / (nannorm(a) * nannorm(b))

def recommend(data):
	
	#Preprocessing involves labelling unrated entries as Nan and also the each user rating is normalised.
	data[data == 0] = np.nan
	normalise(data)
	
	item_list = [i for i in range(data.shape[1]) if nannorm(data[:, i]) != 0]
	for item in item_list:
		
		#Calculates the similarity/distance between items and select the ones whose distance is > 0.
		distances = np.array([[neighbor, cosine(data[:, item], data[:, neighbor])] for neighbor in item_list if item != neighbor])
		similar_items = [int(i) for i in distances[np.where(distances[:, 1] > 0.0), 0][0]]
		total_distance = np.sum(distances[:, 1]) #Used to calculate the weighted average

		for user in np.where(np.isnan(data[:, item]))[0]:
			rating = 0.0

			for similar in similar_items:
				if ~np.isnan(data[user, similar]):
					rating += (distances[np.where(distances[:,0] == similar), 1] / total_distance) * data[user, similar]

			data[user,item] = rating

	return data
	
if __name__ == "__main__":
	
	print("Number of users")
	num_users = int(sys.stdin.readline())

	print("Number of movies")
	num_movies = int(sys.stdin.readline())

	data = []
	with open("data", "r") as handle:
		for line in handle:
			data.append(line.split())

	data = np.array(data, dtype = float)
	normalised_ratings = recommend(data.copy())	

	print(normalised_ratings)
