# STACK DS IN PYTHON

class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def get_stack(self):
		return self.items

	def get_stack_size(self):
		 return len(self.items)


	def reverse_string(stack, string):
		rev_str = ""
		for s in string:
			stack.push(s)
		#print(stack.get_stack())	
		for s in string:
			rev_str += (stack.pop())
		print(rev_str)	


		