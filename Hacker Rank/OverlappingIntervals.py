def OverlapIntervals(arr):
    count = 0;
    if(len(a) > 0):
        arr.sort()
        for i in range(len(a)-1):
            j = i+1
            if(a[i][1] > a[j][0]):
                count+=1
                print(a[i][1], " ", a[j][0], " ", count)
    return count            


if __name__=="__main__":
    a = [[0,0]]
    print(OverlapIntervals(a))

    
