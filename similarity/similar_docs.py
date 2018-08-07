import glob
import shingle
import signature

def get_max(shingles):
	maximum = []

	for key, values in shingles.items():
		maximum.append(max(values))

	return max(maximum)

if __name__ == "__main__":

	shingles = {filename : shingle.shingle(filename) for filename in glob.glob("./*.txt")}
	
	#print(get_max(shingles))
	signatures = signature.signature(shingles, get_max(shingles), 2)

