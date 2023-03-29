'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def xor(i):
            if i == len(nums): 
                return i
            return nums[i]^i^xor(i+1)
        return xor(0)
