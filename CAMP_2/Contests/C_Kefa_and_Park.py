from collections import defaultdict
from functools import cache


class Graph:
    def __init__(self):
        self.answer = 0
        self.neighbours = defaultdict(list)
        self.cats = []

    def addEdge(self, s, e):
        self.neighbours[s].append(e)
    
    @cache
    def solve(self, root, m):
        
        if len(self.neighbours[root]) == 0 and self.cats[root] == 0:
            self.answer += 1

        for child in self.neighbours[root]:
            if m - self.cats[child] >= 0:
                self.solve(child, m-self.cats[child])


def main():
    n, m = (int(_) for _ in input().split())
    cats = [int(_) for _ in input().split()]
    graph = Graph()

    for _ in range(n-1):
        u, v = [int(_) for _ in input().split()]
        graph.addEdge(u-1, v-1)
    graph.cats = cats
    m -= cats[0]
    graph.solve(0, m)
    
    print(graph.answer)

main()