class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #cumulate!
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        if nums[-1]<target: return 0
        i, j = 0, 0
        ans = len(nums) 
        while j < len (nums):
            s = nums[j] if i == 0 else nums[j] - nums[i-1]
            if s >= target:
                ans = min(ans, j-i+1)
                i+=1
            else: j+=1
        
        return ans