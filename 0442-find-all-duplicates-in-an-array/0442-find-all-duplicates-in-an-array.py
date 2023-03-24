class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.append(-1)
        result = [] 
        
        for index in range(len(nums)):
           
            while nums[index] != index + 1: 
                if nums[index] == -1: 
                    break
                
                if nums[index] == nums[nums[index]-1] : 
                    result.append(nums[index])
                    nums[index] = -1
                    
                    break
                
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1] 
        
        return result
    