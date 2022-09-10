class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        diff = 0
        i = 1
        while i<len(nums) and nums[i]-nums[i-1]==0:
            i+=1
        if i <len(nums):
            diff = nums[i]-nums[i-1]
        for i in range(1,len(nums)): 
               if diff*(nums[i]-nums[i-1]) < 0:
                    return False
        return True