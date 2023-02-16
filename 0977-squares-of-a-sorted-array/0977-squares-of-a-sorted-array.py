class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [nums[0]**2]
        sq = []
        a,b = 0,len(nums)-1
        
        while a<b:
            if nums[a]**2 >= nums[b]**2:
                sq.insert(0,nums[a]**2)
                a+=1
            else:
                sq.insert(0,nums[b]**2) 
                b-=1
        sq.insert(0,nums[a]**2)
        return sq