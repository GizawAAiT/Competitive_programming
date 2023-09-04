class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [_ for _ in range(len(nums)) if nums[_]==target]