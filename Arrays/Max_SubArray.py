#THIS IS SOLVED USING KADANE"S ALGORITHM IN O(n) - COMPLEXITY
from pyfiglet import Figlet

def kadane(arr):
    max_current = max_global = arr[0]
    for i in range(1,len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global        






if __name__=="__main__":
    f = Figlet(font='banner3')
    print(f.renderText("STOCK ANALYZER"))
    print("PLEASE ENTER THE DATA RELATED TO STOCKS:")
    days = int(input("NO OF DAYS THE DATA IS AVAILABLE:"))
    price = list(map(int,input("PLEASE ENTER THE CLOSING PRICE OF THE STOCK WITH SPACE FOR {0}:".format(days)).strip().split()))[:days]
    A = []
    A.append(0)
    #print(A)
    #print(days, price[0], A[0])
    for i in range(1,days):
        #print(i, price[i], price[i-1])
        temp = price[i] - price[i-1] 
        A.append(temp)
    max_subarray = kadane(A)
    print("MAX-SUB-ARRAY:",max_subarray)
