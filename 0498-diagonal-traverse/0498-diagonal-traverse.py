class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        iteration = 0
        i, j = 0, 1
        res = []
        while i<j:
            temp = []
            for t in range(i,j):
                temp.append(mat[t].pop(0))
            if j<len(mat): j+=1
            if len(mat[i])==0: i+=1
                
            res.extend(temp) if iteration%2==1 else res.extend(list(reversed(temp)))
            iteration +=1
        return res