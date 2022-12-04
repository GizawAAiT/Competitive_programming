class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        # Dp = [nums[0],max(nums[0],nums[1])]
        a = nums[0]
        b = max(nums[1],nums[0])
        
        i = 2
        while i < len(nums):
            # Dp.append(max(nums[i]+Dp[-2],Dp[-1]))
            t = b
            b = max(a+nums[i],b)
            a = t
            i+=1 
        return b
        # return Dp[-1]
