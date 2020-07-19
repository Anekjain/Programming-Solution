#!/usr/bin/env python
import random
import array

#FISHER-YATES ALGORITHM [IN-PLACE]
def shuffle_deck(arr, n):
	for i in range(n-1, 0 ,-1):
		j = random.randint(0,i+1)
		arr[j], arr[i] = arr[i], arr[j]
	return arr

def intoDeck(arr):
	if 11 in arr:
		i = arr.index(11)
		arr[i] = 'J'
	if 12	 in arr:
		i = arr.index(12)
		arr[i] = 'Q'
	if 13	 in arr:
		i = arr.index(13)
		arr[i] = 'K'
	if 14	 in arr:
		i = arr.index(14)
		arr[i] = 'A'
	return arr


if __name__=="__main__":
	deck  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
	n = len(deck)
	rand_deck = shuffle_deck(deck,n)
	print rand_deck
	dec = intoDeck(rand_deck)
	print dec
