import numpy as np
import sys
import pdb

def merge_buckets(bucket_list):
	
	flag = True
	index = len(bucket_list) - 1

	while flag and (index != 1):
		if bucket_list[index][1] == bucket_list[index - 1][1] == bucket_list[index - 2][1]:
			bucket_list[index - 1][1] += bucket_list[index - 2][1]
			bucket_list.pop(index - 2)
			index -= 2

		else:
			flag = False
	
	return

def motvani(bit, bucket_list, timestamp):

	#Create the first bucket in the stream with size 1
	if not bucket_list:
		if bit == '1':
			bucket_list.append([timestamp, 1])
	
	else:

		#Removes the least recent bucket, if timestamp (of course, mod window_size) is equal to the bucket's timestamp
		if timestamp == bucket_list[0][0]:
			bucket_list.pop(0)

		if bit == '1':
			bucket_list.append([timestamp, 1])
			merge_buckets(bucket_list)
	
	return
		
def estimate(bucket_list, k, timestamp):

	ones = 0
	index = len(bucket_list) - 1
	
	while (index != 0) and (k >= (timestamp - bucket_list[index][0])):
		ones += bucket_list[index][1]
		index -= 1

	return ones

if __name__ == "__main__":

	print("Required window size")
	window_size = int(sys.stdin.readline())

	print("Binary stream size")
	#FIXME
	#stream_size = int(sys.stdin.readline())
	
	#FIXME
	#stream = []
	stream = list("1001010110001011010101010101011010101010101110101010111010100010110010")

	timestamp = 0
	bucket_list = []

	#FIXME
	while timestamp < len(stream):
		#FIXME
		#bit = np.random.randint(2)
		bit = stream[timestamp]

		#We append the new bit into a list which is used to calculate actual count of 1's.
		#FIXME
		#stream.append(bit)
		motvani(bit, bucket_list, timestamp % window_size)

		timestamp += 1
	
	print("Actual number of ones", np.sum(np.array(stream) == '1'))	
	print(estimate(bucket_list, window_size, timestamp))

