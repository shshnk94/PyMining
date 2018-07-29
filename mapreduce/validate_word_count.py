import glob

if __name__ == "__main__":
	special_chars = ".,!?;:-"
	
	for doc in glob.glob("./*.txt"):
		with open(doc, "r") as handle:
			for line in handle:
				for word in line.split():
					print(word.strip(special_chars))
