#!/usr/bin/env python


def Number_Generator(n):
	while(n != 1): 
		if(n%2 == 0):
			n=n/2
			print(n)
		else:
			n=(n*3)+1
			print(n)

def main():
	n = input("Enter Value of n ")
	Number_Generator(n)


if __name__ == "__main__":
	main()
