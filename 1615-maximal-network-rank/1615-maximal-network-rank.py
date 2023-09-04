from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        neighbours = defaultdict(list)
        
        for source, destination in roads:
            neighbours[source].append(destination)
            neighbours[destination].append(source)
            
        maximum_network = 0
        for i in range(n):
            for j in range(i+1, n):
                maximum_network = max(maximum_network, (len(neighbours[i]) + len(neighbours[j]) - int(i in neighbours[j]) ))
                
        return maximum_network
        