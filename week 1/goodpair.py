class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodpair=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]:
                    goodpair += 1
        return goodpair