class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            v=nums.remove(original)
            original*=2
        return original
            