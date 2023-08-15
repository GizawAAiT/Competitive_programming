class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjL = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j]:
                    adjL[i].append(j)
                    adjL[j].append(i) #cross map.
                    
        visited = set()
        
        def dfs(indx):
            que = [indx]
            while que:
                node = que.pop()
                visited.add(node)
                for neigh in adjL[node]:
                    if neigh not in visited:
                        que.append(neigh)
        count = 0
        for indx in range(n):
            if indx not in visited:
                count += 1
                dfs(indx)
        
        return count

                
            