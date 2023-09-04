class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums.append(-1)
        for index in range(len(nums)):
            while nums[index] != index + 1:
                
                if nums[index] == nums[nums[index]-1] or nums[index] == -1: 
                    nums[index] = -1
                    break
                
                # n = nums[index] 
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1] 
         
        result = [] 
        for index, value in enumerate(nums[:-1]):
            if value != index + 1:
                result.append(index+1) 
        
        return result
        
            