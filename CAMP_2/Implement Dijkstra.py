import heapq
from collections import defaultdict

class Edge:
    def __init__(self):
        self.start = None
        self.end = None
        self.weight = float('inf')

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
            

graph = Graph()
graph.addEdge('a', 'b', 2)
graph.addEdge('a', 'c', 4)
graph.addEdge('b', 'd', 2)
graph.addEdge('c', 'd', 8)
graph.addEdge('b', 'c', 1)
graph.addEdge('c', 'b', 4)
graph.addEdge('e', 'd', 9)
graph.addEdge('d', 'e', 7)
print(Dijkstra("a", "e", graph))





