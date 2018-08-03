import glob

def shingle(filename):
	k = 9

	with open(filename, "r") as handle:
		doc = list((handle.readlines())[0])

	'''	
	We slice the shingle of length 'k' from the list of characters from the document,
	Then we hash these slices to reduce them to 4 byte integers.
	'''

	k_shingles = set([hash("".join(doc[index : index + k])) % (2 ** 32) for index in range(len(doc) - k + 1)])

	return k_shingles
	

if __name__ == "__main__":
	
	for filename in glob.glob("*.txt"):
		shingle(filename)
