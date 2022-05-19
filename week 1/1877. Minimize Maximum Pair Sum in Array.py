class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        m=nums[0]+nums[-1]
        for i in range (1, len(nums)//2):
            m=max((nums[i]+nums[-i-1]), m)
        return m    