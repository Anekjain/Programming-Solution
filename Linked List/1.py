#!/usr/bin/env python

# IMPORT
from ll import *

if __name__ == "__main__":
	
	llist = LinkedList()

	llist.head = Node(1)
	second = Node (2)
	third = Node(3)

	llist.head.next = second
	second.next = third

	llist.printlist()
	print " "
	llist.push(4)

	llist.printlist()
