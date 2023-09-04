class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if target <= i + nums[i] :
                target = i
        
        return target == 0