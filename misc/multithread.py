#MULTI-THREADING IN PYTHON

from time import sleep
from threading import *

#THREAD 1
class Hello(Thread):
	def run(self):
		for x in range(5):
			print("Hello")

#THREAD 2
class Hi(Thread):
	def run(self):
		for x in range(5):
			print("Hi")

#CREATING OBJECTS OF CLASSES
t1 = Hello()	
t2 = Hi()

t1.start() # Starting Thread 1
sleep(0.2) # To Avoid collision of two threads.
t2.start() # Starting Thread 2						

t1.join() # This tells the Main thread to wait for until t1 joins Main Thread
t2.join() # This tells the Main thread to wait for until t2 joins Main Thread


print("Bye") # Main Thread due to join function will wait for t1 and t2 to join and then execute.