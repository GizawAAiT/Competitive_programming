class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def flip(l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
                
                
        n = len(nums) #length
        k %=n
        
        flip(0, n-1) 
        flip(0, k-1)
        flip(k, n-1)
        
        
      