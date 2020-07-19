from stack import Stack

def div_by_2(dec_num):
	s = Stack()

	while dec_num > 0:
		remainder = dec_num % 2
		s.push(remainder)
		dec_num = dec_num // 2

	binary = ""
	while not s.is_empty():
		binary += str(s.pop())

	print(binary)		
	


if __name__ == '__main__':
	div_by_2(242)

	