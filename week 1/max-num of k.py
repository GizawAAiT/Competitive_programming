class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=sorted(nums)
        a=0
        b=len(nums)-1
        # for i in range(len(nums)//2):
        c=0
        while a<b:
            t=nums[a]+nums[b]
            if t==k:
                c+=1
                a+=1
                b-=1
            elif t<k:
                a+=1
            else:
                b-=1
        return c
        