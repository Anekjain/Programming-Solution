def Between_Two_Sets(a,b):
    result = []
    for i in range(len(a)-1,-1,-1):
        for j in range(len(a)-1,-1,-1):
            if(i!=j):
                print("BEFORE LOOP: ",a[i],a[j])
                if(a[i]%a[j] == 0):
                    print("AFTER LOOP 1: ",a[i],a[j])    
                    pass
        print("AFTER LOOP 2: ",a[i],a[j])         
        result.append(a[j])            
    return set(result)


def factor(a,b):
    if(a%b==0):
        return True
    else:
        return False

if __name__ == "__main__":
    # a = list(map(int, input().split(" ")))
    # b = list(map(int, input().split(" ")))
    result = Between_Two_Sets([1,2,4,6,8],[24,36])
    print(result)