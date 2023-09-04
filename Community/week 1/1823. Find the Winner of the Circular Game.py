class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        st=[]
        for i in range (1,n+1):
            st.append(i)
        p=-1
        while len(st)>1:
            for i in range(k):
                if p < len(st)-1:
                    p+=1
                else:
                    p=0
            st.pop(p)
            p-=1
        return st[0]
                    
            
       