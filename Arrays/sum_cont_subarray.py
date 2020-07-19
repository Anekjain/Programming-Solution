def sum_cont_subarray(ar,s):
	for i in range(len(ar)):
		sub_sum = 0
		for j in range(i,len(ar)-1):
			while(sub_sum <= s):
				n = ar[i] + arr[j]
			if(n == sum):
				print(i)
			else:
				print(-1)	



if __name__=="__main__":
	for _ in range(int(input())):
		n,s = (input().split())
		s = int(s)
		for _ in range(n):
			arr = list(map(int,input().split()))
			sum_cont_subarray(arr,s)
			
			
