# Problem - To find number of Subet which add up to a given sum
# INPUT : An Array and Sum, [2,4,6,10,16] sum = 16
#OUTPUT : Count of Subset which add up to a given sum. count = 3. i.e {[2,4,6],[6,10],[16]}



def Number_of_Set(arr, sum):
    i = len(arr)
    return rec(arr, sum, i-1)
def rec(arr, sum, i):
#   BASE CONDITION
    if(sum == 0):
        return 1
    elif(sum < 0):
        return 1
    elif(i < 0):
        return 0
    elif(sum < arr[i]):
        return rec(arr, sum, i-1)
    else:
        return rec(arr,sum-arr[i],i-1) + rec(arr, sum, i-1)

if __name__=="__main__":
    arr = [2,4,6,10,16]
    sum = 16
    c = Number_of_Set(arr,sum)
    print(c)
