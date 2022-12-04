class Solution(object):
    def hIndex(self, cit):
        """
        :type citations: List[int]
        :rtype: int
        """       
        if len(cit)==1 and cit[0]==0:
            return 0
        cit=sorted(cit,reverse=True)
        i=0
        c=1
        while i<len(cit) and c <= cit[i]:
            i+=1
            c+=1
        return c-1
