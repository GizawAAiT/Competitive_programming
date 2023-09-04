class Solution:
    def onesMinusZeros(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        row, col = defaultdict(int), defaultdict(int)
        for i in range(r):
            for j in range(c):
                row[i] += mat[i][j]
                col[j] += mat[i][j]
        res = [[] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                res[i].append(2*(row[i]+col[j])-(r+c))
        return res