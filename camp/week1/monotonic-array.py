class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        slop = set()
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                slop.add(1 if nums[i]> nums[i-1] else -1)
            if len(slop) >1: return False
        return True