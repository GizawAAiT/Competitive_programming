class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        while l<len(nums):
            r = len(nums)-1
            while r > l:
                if nums[r] == nums[l]:  
                    nums.pop(r)
                r-=1
            l+=1
            
        