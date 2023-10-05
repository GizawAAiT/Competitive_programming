from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        answer = 0
        heap = [(0, k)]
        visited = set()
        
        while heap:
            cost, node = heapq.heappop(heap)
           
            if node not in visited:
                answer = max(answer, cost)
                visited.add(node) 
            for child, weight in graph[node]: 
                if child not in visited:
                    heapq.heappush(heap, (weight+cost, child))
        
        return answer if len(visited) == n else -1
        




        
