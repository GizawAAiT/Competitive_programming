class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(1,len(nums)+1):
            if (i ==len(nums) or nums[-i-1]<i) and nums[-i]>=i :
                return i
        return -1