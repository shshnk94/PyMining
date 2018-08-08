import glob
import sys
import shingle
import signature
import lshashing

def get_max(shingles):
	maximum = []

	for key, values in shingles.items():
		maximum.append(max(values))

	return max(maximum)

if __name__ == "__main__":

	shingles = {filename : shingle.shingle(filename) for filename in glob.glob("./*.txt")}
	
	print("Enter number of bands (b) and number of rows in each (r)")
	bands = int(sys.stdin.readline())
	rows = int(sys.stdin.readline())
	signatures = signature.signature(shingles, get_max(shingles), bands * rows)
	
	candidate_pairs = lshashing.locality_sensitive_hashing(signatures, bands, rows)
	print(candidate_pairs)

