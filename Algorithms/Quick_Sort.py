def Quick_Sort(arr, left, right):
    # Array is inorder Condition / One element Condition.
    if(left >= right):
        return
    

    #CHOOSING PIVOT ELEMENT
    pivot_index = (left + right)//2
    pivot = arr[pivot_index]
  
    #Get The Partition Index
    index = Partition(arr, left, right, pivot)

    #Quick Sort on left and right partition.
    Quick_Sort(arr, left, index-1)
    Quick_Sort(arr, index, right)

    return arr
    
def Partition(arr, left, right, pivot):
    while(left <= right):
        while(arr[left] < pivot):
            left+=1
        while(arr[right] > pivot):
            right-=1
        if(left <= right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left       

if __name__=="__main__":
    arr = list(map(int, input("Quick Sort Elements: \n").split()))
    arr = Quick_Sort(arr, 0, len(arr)-1)
    print(arr)
