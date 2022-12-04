class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        vals = sorted([nums[0],nums[1]])
        
        for n in nums[2:]:
            if n > vals[1]:
                vals[0], vals[1] = vals[1], n
            elif n > vals[0]:
                vals[0] = n
        return (vals[0]-1)*(vals[1]-1)