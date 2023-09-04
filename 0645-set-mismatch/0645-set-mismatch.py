class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        result = []
        
        for index in range(len(nums)):
           
            while nums[index] != index + 1: 
                if nums[index] == -1:
                    break
                if nums[index] == nums[nums[index]-1] : 
                    
                    result.append(nums[index]) 
                    nums[index] = -1
                
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1] 
                
        for i, n in enumerate(nums):
            if n == -1:
                result.append(i+1)
            
        return result