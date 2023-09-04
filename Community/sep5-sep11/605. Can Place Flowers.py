class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if n ==0:
            return True
        if len(f) ==1:
            n-=int(f[0]==0)
            return n ==0
        if f[0]+f[1] == 0:
            n-=1
            f[0]=1
        i = 1
        
        while i < len(f)-1:
            if n ==0:
                return True
            if f[i-1]+f[i+1] == 0 and f[i]==0:
                n-=1
                f[i]=1
            i+=1
        if f[-1]+ f[-2] ==0:
            n-=1
        print(f,n)
        return n==0
            
                
