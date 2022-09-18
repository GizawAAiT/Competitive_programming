class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R,C=len(matrix),len(matrix[0])
        r0,c0=set(),set()
        for i in range(R):
            for j in range(C):
                if matrix[i][j]==0:
                    r0.add(i)
                    c0.add(j)
        # print(f"r0: {r0} c0: {c0}")
        for i in range(R):
            for j in range(C):
                if i in r0 or j in c0:
                    matrix[i][j]=0
        return matrix