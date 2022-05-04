class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        fc=0
        a=b=0
        maxCons= 0
        while b<len(nums):
            while fc <= k and b<len(nums):
                if nums[b]==0:
                    fc +=1
                b +=1
            
            if b<len(nums) and nums[b]==0 or nums[b-1]==0 and fc>k: 
                maxCons=max(maxCons,b-a-1)
            else:
                maxCons=max(maxCons,b-a)
                
            print (maxCons)
            while a<len(nums) and nums[a]==1:
                a +=1
            a+=1
            fc-=1
        return maxCons
        