# This is a global variable
a = 10

def Global_Variable():
	global a
	print('Global ', a)

Global_Variable() #accessing Global Variable


def Local_Variable():
	a = 11
	print('Local ', a)

Local_Variable() #accessong local variable	

#How to access both Global and local Variable 
# with same name

def Global_Local_variable():
	a = 11
	x = globals()['a'] 
	#[SYNATAX - globals()['NAME'], 
	# as it gives all globals variable
	print('Local', a)
	print('Global ', x)
	# change global variable value to 15
	globals()['a'] = 15

Global_Local_variable()
print("Global Changed ", a)

