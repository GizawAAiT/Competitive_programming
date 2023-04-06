class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        reachable = set()
        
        for u, v in edges:
            reachable.add(v)
        
        unreachable = []
        for vertex in range(0, n):
            if vertex not in reachable:
                unreachable.append(vertex)
                
        return unreachable