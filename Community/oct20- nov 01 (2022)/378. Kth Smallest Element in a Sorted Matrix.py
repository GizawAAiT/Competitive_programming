class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        m, N = [], len(matrix) 
        size = N**2 - k+1
        for i in range(N):
            for j in range(N):
                heapq.heappush(m, matrix[i][j])
                if len(m) > size:
                    heapq.heappop(m)
        return heapq.heappop(m)
        
                
                    