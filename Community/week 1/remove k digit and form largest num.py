class Solution(object):
    def removeKdigits(self, n, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
#         if len(n)==1:
#             return str(0)
        if len(n) ==1:
            return str(0)
        m=[]
        for i in range(len(n)):
            m.append(int(n[i]))
        n=m
        st=[]
        st.append(n[0])
        i=1
        while i<len(n) and k>0:
            if len(st)>0:
                if n[i]>=st[-1]:
                    st.append(n[i])
                    i+=1
                else:
                    st.pop()
                    k-=1
                    if k==0:
                        break
            else:
                st.append(n[i])
                i+=1
                
        while i<len(n):
            st.append(n[i])
            i+=1
        while k>0:
            st.pop()
            k-=1
        if len(st)!=0:
            i=(st[0])
            while i==0 and st:
                st.pop(0)
                if len(st)>0:
                    i=st[0]
        if len(st) ==0:
            return str(0)
        return "".join(str(j) for j in st)
            
            
            
        
            
                          
                          