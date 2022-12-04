class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        b=9
        n=88
        u=b/n
        print floor(u)
        u=-u
        u=ceil(u)
        print (-u)
        x=["+","-","*","/"]
        st=[]
        for t in tokens:
            if t not in x:
                st.append(int(t))
            else:
                if t=='+':
                    st[-2] +=st[-1]
                    st.pop()
                elif t=="-":
                    st[-2]=st[-2]-st[-1]
                    st.pop()
                elif t=="*":
                    st[-2]=st[-2]*st[-1]
                    st.pop()
                elif t=="/":
                    if st[-1]*st[-2]<0 : 
                        u=float(st[-2])/st[-1]
                        u=-u
                        u=floor(u)
                        st[-2]=-int(u)
                    else:
                        st[-2]=st[-2]//st[-1]
                    st.pop()
        return st[-1]