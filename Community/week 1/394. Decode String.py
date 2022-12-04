class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in range(len(s)):
            if s[i]!="]":
                st.append(s[i])
            else:
                pic=st[-1]
                st.pop()
                while st[-1] !="[":
                    pic = st[-1] + pic
                    st.pop()
                st.pop()
                multiplier=""
                while st and st[-1].isdigit():
                    multiplier = st[-1] + multiplier
                    st.pop()
                st.append(int(multiplier)*pic)    
        return "".join(st)
            
            
            