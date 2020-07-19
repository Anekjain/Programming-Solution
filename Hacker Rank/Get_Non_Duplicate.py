#Getting a Non Duplicate Number from an array  
nums = [1,1,2,2,3]
for i in range(len(nums)):
        if nums.count(nums[i])==1:
                print("NON-DUPLICATE NUMBER: ",nums[i])
