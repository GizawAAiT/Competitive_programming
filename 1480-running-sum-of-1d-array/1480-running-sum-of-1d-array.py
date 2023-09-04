class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for _ in range(1, len(nums)):
            nums[_] += nums[_-1] 
        return nums