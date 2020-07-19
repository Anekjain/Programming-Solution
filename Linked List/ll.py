#!/usr/bin/env python

class Node:
	def __init__(self, data):
		self.data  = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	def push(self, data):
		data = Node(data)
		data.next = self.head
		self.head = data

	def insert_after(self, prev_node, data):
		if(prev_node == None):
			print ("Previous Node is NULL")
		data = Node(data)
		data.next = prev_node.next
		prev_node.next = data.next

	def append(self, data):
		data = Node(data)
		
		# IF NO NODE IS PRESENT THEN IT BECOMES THE FIRST NODE
		if(self.head == None):
			self.head = data
		return
		
		#TRAVERSE TILL LAST NODE
		last = self.head
		while(last.next):
			last = last.next
		last.next = data
