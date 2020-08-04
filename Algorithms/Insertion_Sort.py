def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j] > key):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key    
                
    return arr            

if __name__=="__main__":
    arr = list(map(int, input("Enter Elements to be Sorted Using Insertion Sort !\n").split()))
    arr = Insertion_Sort(arr)
    print(arr)
