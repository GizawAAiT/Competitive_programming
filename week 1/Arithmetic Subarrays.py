class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        boole=[]
        # sub=[]
        for i in range(len(l)):
            sub=nums[l[i]:(int(r[i])+1)]
            sub=sorted(sub)
            d=sub[1]-sub[0]
            b=True
            for j in range(2,len(sub)):
                if d!=sub[j]-sub[j-1]:
                    b=False
                    break
            boole.append(b)
        return boole
                    
                