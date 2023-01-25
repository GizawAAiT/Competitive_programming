class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        while l<r:
            while l<len(nums) and nums[l]==0: l+=1
            while r>0 and nums[r]!=0: r-=1
            if l<r:
                nums[l], nums[r]=nums[r], nums[l]
        l, r = 0, len(nums)-1
        while l<r:
            while l<len(nums) and nums[l]!=2: l+=1
            while r>0 and nums[r]==2: r-=1
            if l<r:
                nums[l], nums[r]=nums[r], nums[l]
        
                   
                