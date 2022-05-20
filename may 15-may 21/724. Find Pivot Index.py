class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total+=i
        
        i=sum=0
        
        while i < len( nums):
            if sum ==(total - nums[i])/2:
                return i
            sum+=nums[i]
            i+=1
        return -1
    

        