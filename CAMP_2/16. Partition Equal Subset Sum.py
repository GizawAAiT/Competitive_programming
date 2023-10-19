class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False

        target = total // 2
        @cache
        def dp(target, indx):
            if target == 0: return True
            if target < 0 or indx >= len(nums):
                return False
            return dp(target, indx+1) or dp(target-nums[indx], indx+1)

        return dp(target, 0)