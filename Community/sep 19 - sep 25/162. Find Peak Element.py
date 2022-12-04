class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1 or nums[0]>nums[1]: return 0

        l,r = 0,len(nums)-1
        while l<r-1:
            m=l+(r-l)//2
            if nums[m]<nums[m+1] :l=m              
            else:r=m
        return r
 
        