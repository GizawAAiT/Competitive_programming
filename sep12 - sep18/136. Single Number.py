class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums = sorted(nums)
        if nums[1]!=nums[0]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                return nums[i]
        