class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return -int(nums[0]!= target)
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums)-1
        a,b = 0,len(nums)-1
        while a<b-1:
            m = (a+b)//2
            if nums[m]==target: 
                return m
            if nums[m] > target:
                b = m
            else:
                a = m
        return -1