class Solution(object):
    def maxArea(self, n):
        """
        :type height: List[int]
        :rtype: int
        """
        
        m=0
        i=0
        j=len(n)-1
        while i<j:
            if n[i]<n[j]:
                m=max(n[i]*(j-i),m)
                i+=1
            else:
                m=max(n[j]*(j-i),m)
                j-=1
            
        return m