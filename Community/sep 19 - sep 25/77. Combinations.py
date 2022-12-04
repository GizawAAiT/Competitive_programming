class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        dp=[[i for i in range(1,k+1)]]
        def nxt(arr):
            if arr[-1]!=n: 
                new=arr.copy()
                new[-1]+=1
                return new 
            new=[]           
            i=0
            while i<k and arr[-1-i]==n-i: 
                i+=1
            if i==k: return -1
            i=k-i-1
            for j in range(k):
                if j<i: new.append(arr[j])
                elif j==i: new.append(arr[j]+1)
                else: new.append(new[-1]+1)
            return new
        
        while True:
            a=nxt(dp[-1])
            if a==-1: break
            dp.append(a)
        return dp
                        
                    