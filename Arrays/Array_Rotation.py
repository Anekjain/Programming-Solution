#!/usr/bin/env python

def array_rotation(ar, d, n):
	if (d == 0 or d == n):
		return;
	i = d;
	j = n-d;
	while(i != j):
		if(i < j):
			swap(arr, d-i, d+j-i, i)
			j -= i
		else:
			swap(arr, d-i, d, j)
			i -= j
	swap(arr, d-i, d, i)
	


def main():
	arr = [1,2,3,4,5]
	array_rotation(arr, 2, len(arr))



