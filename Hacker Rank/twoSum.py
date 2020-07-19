def twoSum(nums, target):
    #USING ONE TIME HASH TABLE
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]

if __name__=="__main__":
    n = [3,2,4]
    t = 6
    print(twoSum(n,t))



                

                    
