class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for sub, man in enumerate(manager):
            graph[man].append(sub)
        
        h = [(0, headID)]
        time = 0
        while h:
            time, node = heappop(h) # time = overall time until the 'node'
            for child in graph[node]:
                heappush(h, (time + informTime[node], child))
        
        return time


