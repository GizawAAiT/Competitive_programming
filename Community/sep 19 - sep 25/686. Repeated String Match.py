class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
            # if set(a)!=set(b):return -1
            
            def firstMatch(a,b):
                b=b[:len(a)] if len(b)>len(a) else b
                mxd=a+a[:len(b)-1]
                for i in range(len(mxd)-len(b)+1):
                    if mxd[i:i+len(b)]==b:
                        return i
                return -1
            i,j=firstMatch(a,b),0
            if i==-1:return -1
            c,la=1,len(a)
            while j<len(b):
                if a[i]!=b[j]:
                    return -1
                i,j = (i+1)%la,j+1
                if i==0 and j<len(b):
                    c+=1
            return c
            
                