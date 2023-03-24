class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for index in range(len(nums)):
           
            while nums[index] != index + 1: 
              
                if nums[index] == nums[nums[index]-1] : 
                    
                    return nums[index]
                
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1] 
        