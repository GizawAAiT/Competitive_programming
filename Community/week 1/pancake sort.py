class Solution(object):
    def pancakeSort(self, n):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n=list(n)
        l=len(n)
        a=[]
        while len(n)>1:
            p=n.index(max(n))+1
            if p==1:
                n=reversed(n)
                
                a.append(l)
                
            elif p < len(n):
                sub=n[:p]
                n[:p]=reversed(sub)
                sub=n
                n=reversed(sub)
                a.append(p)
                a.append(l)
                
            n=list(n)
            n.pop()
            l-=1
        return a

        
            
                
