class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        #shift zeros to the right
        i = 0
        while i<len(nums) and nums[i] != 0: i+=1 
        j = i+1
        while j<len(nums):
            while i<len(nums) and nums[i] != 0:
                i+=1
                
            while j<len(nums) and nums[j] == 0:  
                j+=1
            
            if i<len(nums) and j < len(nums):
                nums[i], nums[j] = nums[j], nums[i] 
        return nums