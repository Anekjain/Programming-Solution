def Selection_Sort(arr):
    arr1 = []
    for i in range(len(arr)):
        temp = min(arr[:])
        arr1.append(temp)
        arr.remove(temp)
    del arr
    return arr1



if __name__=="__main__":
    arr = list(map(int,input("Enter Elements to bo sorted !\n").split()))
    arr = Selection_Sort(arr)
    print(arr)
