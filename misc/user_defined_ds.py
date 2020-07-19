#!/usr/bin/env python

class os_ds:
	arr_time = []
	process = []
	burst_time = []
	
	def __init__(self, arr_time, process, burst_time):
		self.arr_time = arr_time
		self.process = process
		self.burst_time = burst_time
	
	def  printOSProcess(self):
		print self.process 
		print self.arr_time 
		print self.burst_time 
			
		

if __name__ == "__main__":
	arr_time = [0,1]
	process = ['P1', 'P2']
	burst_time = [12, 1]
	os = os_ds(arr_time, process, burst_time)
	os.printOSProcess()

	
		
