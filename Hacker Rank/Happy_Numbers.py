
def Happy_Number(n,loop_count):
    l = []
    sum = 0
    loop_count += 1
    

    if(len(l) > 0):
        l.clear() 
    
    for i in str(n):
        i = int(i)
        l.append(i*i)

    for i in l:
        i = int(i)
        sum += i
        print(sum)
        while(sum == 1):
            break
        
        Happy_Number(sum, loop_count)
   
    
    

    return "True"
   
        


if __name__=="__main__":
    n = 12
    loop_count = 0
    print(Happy_Number(n, loop_count))
    
