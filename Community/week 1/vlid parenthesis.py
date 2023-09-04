class Solution(object):
    def isValid(self, ch):
        """
        :type s: str
        :rtype: bool
        """
        ch=str(ch)
        b=True
        dv={'(':')','[':']','{':'}'}
        if ch[0] not in dv:
            return False
        st=[]
        st.append(ch[0])
        for i in range(1,len(ch)):
            if len(st)!=0:
                if dv[st[-1]]==ch[i]:
                    st.pop()
                else:
                    if ch[i] not in dv:
                        return False
                    st.append(ch[i])
            else:
                if ch[i] not in dv:
                    return False
                st.append(ch[i])
        if len(st)!=0:
            return False
        return b                      
            
                       
            

            
           
                       

        