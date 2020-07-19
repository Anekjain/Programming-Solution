# A NUMBER IS IN FIBNOCCI SERIES IF ITS (5*N*N + 4)|(5*N*N - 4) IS A PERFECT SQUARE
from math import sqrt

def is_perfect_square(n):
	s = int(math.sqrt(n))
	return s*s == n

def is_Fibnocci(x):
	return is_perfect_square(5*x*x + 4) or is_perfect_square(5*x*x - 4)

for i in range (1,11):
	if(is_Fibnocci(i) == True):
		print i, "is a fibnocci no"
	else:
		print i, "is a not a fibnocci no"