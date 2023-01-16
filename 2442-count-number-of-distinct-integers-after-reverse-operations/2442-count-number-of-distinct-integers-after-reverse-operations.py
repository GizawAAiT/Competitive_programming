class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums.extend([int(''.join(reversed(list(str(n))))) for n in nums])  
        return len(set(nums))