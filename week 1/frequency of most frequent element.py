class Solution(object):
    def maxFrequency(self, n, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=sorted(n)
        i=0
        j=1
        s=0
        a=1
        d=[]
        if len(n)==1:
            return 1
        s=n[1]-n[0]
        while j<len(n) and i<len(n):
              
            if s<=k:
                a+=1
                j+=1
                d.append(a)
                if j<len(n):
                    s+=(n[j]-n[j-1])*(j-i)
            else:
                i+=1
                
                a-=1
                d.append(a)
                s-=n[j]-n[i-1]
        # s+=(n[j]-n[j-1])*(j-i)
        return max(d)