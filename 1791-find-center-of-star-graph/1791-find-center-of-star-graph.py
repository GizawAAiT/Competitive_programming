from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        count_of_neighbours = defaultdict(int)
        for u, v in edges:
            count_of_neighbours[u] += 1
            count_of_neighbours[v] += 1
        
        if count_of_neighbours[edges[0][0]] == len(edges):
            return edges[0][0]
        return edges[0][1]