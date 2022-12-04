class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<=3:
            return max(nums)
        
#       plan 1. start robbing from house 1.
        a = nums[0]
        b = max(nums[0],nums[1])
        
        i = 2
        while i < len(nums)-1:
            t = b
            b = max(a+nums[i],b)
            a = t
            i+=1 
            
            
#        plan 2. start robbing from house 2.
        c = nums[1]
        d = max(nums[1],nums[2])
        
        i = 3
        while i < len(nums):
            t = d
            d = max(c+nums[i],d)
            c = t
            i+=1 
        return max(b,d)
