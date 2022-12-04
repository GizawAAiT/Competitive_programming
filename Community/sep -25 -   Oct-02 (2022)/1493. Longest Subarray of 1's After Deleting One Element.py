class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        i=0
        while i<len(nums) and nums[i]==0:
            i+=1
        j, middle = i+1, 0
        res = 0
        while j<len(nums):
            if nums[j]==1: j+=1
            elif middle == 0: 
                middle = j 
                j+=1
            else:
                res = max(res, j-i-1)
                i=middle+1
                middle=j
                j+=1
        print("res=",(res),(i,j))
        if res ==0: 
            res =j-i if middle==0 and i>0 and j-i>1 else min(len(nums)-1,j-i-1) 
        else: res = max(res, j-i-1)
        return res
        
        