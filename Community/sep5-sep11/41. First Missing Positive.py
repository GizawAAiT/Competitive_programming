class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = set(nums)
        
        i = 1
        while i in n:
            i+=1
        return i