class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # indices = []
        nums.sort()
        
        indices = [_ for _ in range(len(nums)) if nums[_]==target]
        # for _ in range(len(nums)):
        #     if nums[_] == target:
        #         indices.append(_)
        return indices