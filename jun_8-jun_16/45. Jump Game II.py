class Solution:
    def jump(self, n: List[int]) -> int:
        #windowing
        p1 = p2 = 0
        c=0
        while p2 < len(n)-1:
            f = p1
            for i in range(p1,p2+1):
                f = max(f,i+n[i])
            p1=p2+1
            p2=f
            c+=1
        return c
        
