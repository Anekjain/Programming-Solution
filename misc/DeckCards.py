#!/usr/bin/env python
import random


#FISHER-YATES ALGORITHM [IN-PLACE]
def shuffle_deck(arr, n):
	for i in range(n-1, 0, -1):
		j = random.randint(0, i+1)
		arr[j], arr[i] = arr[i], arr[j]
	return arr

# GETTING J,Q,K,A values
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

#Getting an randomized SET of CARDS
def getCards():
	deck  = [2,3,4,5,6,7,8,9,10,11,12,13,14]
	n = len(deck)
	rand_deck = shuffle_deck(deck,n)
	#print rand_deck
	dec0 = (rand_deck)
	dec1 = (rand_deck)
	dec2 = (rand_deck)
	dec3 = (rand_deck)
	set = dec0 + dec1 + dec2 + dec3
	set = shuffle_deck(set, len(set))
	return set

#DEALING CARDS TO TWO OPPONENTS
def Card_Dealing(c):
	cards = c
	Player_A = []
	Player_B = []
	for i in range(0, len(cards)-1, 1):
		if(i%2 == 0):
			Player_A.append(cards[i])
		else:
			Player_B.append(cards[i])
	return Player_A, Player_B

# GAME LOGIC - 1
def Game(player1, player2):
	res = None
	count = 0
	print ("GAME FUNCTION")
	print (player1)
	print (player2)
	while(len(player1) != 0 and len(player2) != 0):
		# HERE A has HIGHER RANK CARD than B
		if( player1[0] > player2[0] ):
			player1.append(player1.pop(0))
			player1.append(player2.pop(0))
			count += 1
			print(count, player1)
		# HERE A has LOWER RANK CARD than B
		elif( player1[0] < player2[0] ):
			player2.append(player2.pop(0))
			player2.append(player1.pop(0))
			count += 1
			print(count, player2)
		# HERE A has EQUAL RANK CARD to B
		elif( player1[0] == player2[0] ):
			count += 1
			print(count, " War")
			War(player1, player2)
	if(len(player1) == 0):
		res = 0
	elif(len(player2) == 0):
		res = 1
	print("GAME AFTER")
	print(count)
	print(player1)
	print(player2)
	return res

#GAME LOGIC - WAR
def War(player1, player2):
	temp = []
	# A CARDS on TABLE
	temp.append(player1.pop(0))
	temp.append(player1.pop(1))
	# B Cards on TABLE
	temp.append(player2.pop(0))
	temp.append(player2.pop(1))
	#WAR WON BY A
	if(player1[0] > player2[0]):
		player1.extend(temp)
		del temp[:]
	#WAR WON BY B
	elif(player1[0] < player1[0]):
		player2.extend(temp)
		del temp[:]
	#AGAIN WAR
	elif(player1[0] == player2[0]):
		War(player1,player2)
	
	return player1, player2


#MAIN FUNCTION
if __name__=="__main__":
	Cards = getCards()
	print ("SET OF CARDS:")
	print (Cards)
	A, B = Card_Dealing(Cards)
	print ("A - CARDS:")
	print (A)
	print ("B - CARDS:")
	print (B)
	result = Game(A, B)
	if(result == 0):
		print("PLAYER A WON THE GAME")
	elif(result == 1):
		print("PLAYER B WON THE GAME")

