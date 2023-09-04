class Solution:
    def getRow(self, n: int) -> List[int]:
        if n < 2:  
            return [1 for _ in range(n+1)]
        
        b = self.getRow(n-1)
        c = b[:]
        for i in range(1, len(b)):
            c[i] += b[i-1]
        c.append(1)
        return c
    