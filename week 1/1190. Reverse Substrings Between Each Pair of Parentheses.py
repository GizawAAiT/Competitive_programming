class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        print len(s)
        
        # ch=[]
        # if s[0]=="(":
        #     i=0
        #     beg=""
        #     while s[i]!="(":
        #         beg +=s[i]
        #     ch.append(beg)
        # else:
        st=[]
        i=0
        while i<len(s):
            if s[i]=="(":
                st.append(i)
            elif s[i]==")":
                string=s[st[-1]+1:i]
                # print string
                string="".join(reversed(string))
                s=s[:st[-1]] + string + s[i+1:] 
                st.pop()
                i-=2
                print ("s=",s)
            i+=1
        if len(st)!=0:
            string=s[st[-1]+1:len(s)-1]
            s="".join(reversed(string))
        print st
        return s