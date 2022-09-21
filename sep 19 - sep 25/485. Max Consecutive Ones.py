class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # print(nums[0])
        i=0
        mx,c=0,0
        while i<len(nums):
            if nums[i]==0:
                mx=max(mx,c)
                c=0
            else: c+=1
            i+=1
        mx=max(mx,c)
        return mx