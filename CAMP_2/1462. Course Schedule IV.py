class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]: 

        answer = [[False ]*n for _ in range(n)]
        for u, v in prerequisites:
            answer[u][v] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    answer[i][j] = answer[i][j] or (answer[i][k] and answer[k][j]) 
        # matrix[i][j] or (matrix[i][k] and matrix[k][j])
        result = []
        for u, v in queries:
            result.append(answer[u][v])
        return result





        