class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums = sorted(nums)
        major = nums[0]
        f = 1
        i = 1 
        while i<len(nums):
            if nums[i]==major:
                f+=1
            else:
                f = 1
                major = nums[i]
            if f > len(nums)/2:
                return major
            i+=1
                
           