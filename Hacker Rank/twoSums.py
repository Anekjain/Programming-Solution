def twoSum(self, nums, target):
	for i in range(len(nums)):
		x = target - nums[i]
		if x in nums[i+1:]:
			return [i, nums.index(x)]

if __name__=="__main__":
    n = [3,3]
    t = 6
    print(twoSums(n,t))

    

		    

			
