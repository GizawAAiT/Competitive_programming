class Solution:
    def canReach(self, A: List[int], s: int) -> bool:
        
        visited = set()
        Q = set()
        Q.add(s)
        visited.add(s)
        
        while Q:
            s = Q.pop()
            if A[s] == 0:
                return True
            
            for indx in (s+A[s],s-A[s]):
                if indx < len(A) and indx >= 0 and indx not in visited:
                    Q.add(indx)
                    visited.add(indx)
            
        return False   
            

        