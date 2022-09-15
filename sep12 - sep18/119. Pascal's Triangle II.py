class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        
        def binomial(n,r):
            if r == 0:
                return 1
            if r == 1:
                return n
            N = D = 1
            for i in range(n-r+1,n+1):
                N *= i
            for i in range(1,r+1):
                D *= i
            return N//D
        
#         use the binomial function and collect the coefficients
        row = []
        for i in range(rowIndex//2 + 1): 
            row.append(binomial(rowIndex,i))
        
        i = (rowIndex-1)//2
        while i>=0:
            row.append(row[i])
            i-=1
        return row
            