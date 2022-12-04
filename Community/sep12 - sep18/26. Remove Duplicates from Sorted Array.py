class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        i = 1
        while i < len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)+1
                
        