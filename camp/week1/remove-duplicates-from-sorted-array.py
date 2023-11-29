class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        for right in range(len(nums)):
            if nums[right] not in seen:
                nums[i] = nums[right]
                i += 1

            seen.add(nums[right])
        
        for _ in range(len(nums)-i):
            nums.pop()

        
