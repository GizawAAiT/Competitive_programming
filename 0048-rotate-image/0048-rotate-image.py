class Solution:
    def rotate(self, nums: List[List[int]]) -> None:        
        n = len(nums)
        if n ==1:
            return nums
        
        m = 0
        while m < n//2:
            for i in range(n-1-2*m):
                
                temp = nums[m][m+i]
                nums[m][m+i] , nums[-1-m-i][m], nums[-1-m][-1-m-i], nums[m+i][-1-m] = nums[-1-m-i][m], nums[-1-m][-1-m-i], nums[m+i][-1-m], temp 

            m +=1