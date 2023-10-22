class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans, left = len(nums), 0
        count = 1
        for right in range(1, len(nums)):
            count += nums[right] != nums[right-1]
            while nums[right] - nums[left] > len(nums)-1: 
                count -= nums[left+1] != nums[left]
                left += 1
            ans = min(ans, len(nums)- count)
        ans = min(ans, len(nums)- count)
        return ans
