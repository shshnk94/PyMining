import math

#get_prime(number) generates the smallest prime greater than or equal to 'number'

def get_prime(number):	
	
	flag = True
	num = number + 1

	while flag and num < 100:

		i = 2
		while (i <= math.sqrt(num)) and (num % i != 0):
			i += 1

		if i > math.sqrt(num):
			flag = False
		else:
			num += 1

	return num

