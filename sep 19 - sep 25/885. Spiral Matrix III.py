class Solution:
    def spiralMatrixIII(self, r: int, c: int, ri: int, ci: int) -> List[List[int]]:
        def bound(i,j):
            return i>=0 and j>=0 and i<r and j<c
        
        count=1
        jump =1
        ans=[[ri,ci]]
        while count<r*c:
            for _ in range(jump):
                ci+=1
                if bound(ri,ci):
                    ans.append([ri,ci])
                    count +=1
            for _ in range(jump):
                ri+=1
                if bound(ri,ci):
                    ans.append([ri,ci])
                    count +=1
            jump+=1
            for _ in range(jump):
                ci-=1
                if bound(ri,ci):
                    ans.append([ri,ci])
                    count +=1
            for _ in range(jump):
                ri-=1
                if bound(ri,ci):
                    ans.append([ri,ci])
                    count +=1
            jump+=1
        return ans
            
        
            