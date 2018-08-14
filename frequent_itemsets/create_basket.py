import sys

"""
Creates a market basket as mentioned in Exercise 6.1.1 of MMDS.
To create the one in 6.1.3 replace "if basket % item == 0" by "if item % basket == 0"
Also, change the filename if required.
"""

if __name__ == "__main__":

	num_items = int(sys.stdin.readline())
	num_baskets = int(sys.stdin.readline())
	
	basket = 1
	market_basket = []
	while basket <= num_baskets:
		item = 1
		transaction = []
	
		while item <= num_items:
			if item % basket == 0:
				transaction.append(str(item))
			
			item += 1

		market_basket.append(transaction)
		basket += 1
	
	with open("opp_integers", "w") as handle:
		for row in market_basket:
			handle.write(",".join(row) + "\n")
