class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        s = "1"
        for i in range(n-1):
            s = self.say(s)
        return s
    def say(self,nm):
        
        st = []
        c = 0
        i = 0
        t = nm[0] 
        while i < len(nm):
            if t == nm[i]:
                c+=1
            else:
                st.append(str(c)+t)
                t = nm[i]
                c = 1
            i+=1
        st.append(str(c)+t) 
        return "".join(st)
