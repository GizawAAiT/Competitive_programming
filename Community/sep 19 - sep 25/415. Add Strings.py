class Solution:
    def addStrings(self, n1: str, n2: str) -> str:
        res=[]
        rem=0
        while n1 or n2 or rem:
            v1,v2=int(n1[-1]) if n1 else 0,int(n2[-1]) if n2 else 0 
            r = v1+v2+rem
            rem = r//10
            res.append(str(r%10))
            n1,n2=n1[:-1],n2[:-1]
        return "".join(list(reversed(res))) 
            