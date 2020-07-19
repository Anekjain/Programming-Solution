import random
def Binary_Search(x, start, end, key):
    if(end>=start):
        mid = int(start + (end-start)/2)
        if x[mid] == key:
            return (x[mid], mid)
        elif x[mid] > key:
            return Binary_Search(x, start, mid-1, key)
        else:
            return Binary_Search(x, mid+1, end, key)
    else:
        return -1

if __name__=="__main__":
    x = []
    for i in range(10000):
        x.append(random.randint(0,100000000))
    x.sort()
    key = random.choice(x)
    print(key)
    start = 0
    end = len(x)-1
    print(start, end)
    res, mid = Binary_Search(x, start, end, key)
    print(res, mid)
    
    


    
