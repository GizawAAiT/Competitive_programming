import heapq
from collections import defaultdict

# class Edge:
#     def __init__(self):
#         self.start = None
#         self.end = None
#         self.weight = float('inf')

class Graph:
    def __init__(self):
        self.neighbours = defaultdict(list)
        self.parent = {}
    
    def addEdge(self, start, end, weight):
        self.neighbours[start].append((weight, end))

def Dijkstra(start, end, graph):
    heap = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        if node == end:
            return cost
        
        for weight, child in graph.neighbours[node]:
            heapq.heappush(heap, (cost+weight, child))
            
# Adding example usage
graph = Graph()  # 26.1
graph.addEdge("A", "B", 4)  #26.2
graph.addEdge("A", "C", 2)  # 26.3
graph.addEdge("B", "C", 5)  # 26.4
graph.addEdge("B", "D", 10) # 26.5
graph.addEdge("C", "D", 3)  # 26.6
start = "A"  # 26.7
end = "D"    # 26.8
print(Dijkstra(start, end, graph))  # Expected output: 14   #26.9




