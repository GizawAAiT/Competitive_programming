class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        
        hashMap = defaultdict(list)
        for u, v in dislikes:
            hashMap[u].append(v)
            hashMap[v].append(u)
            
        color = [0 for _ in range(n+1)]
            
        def dfs(u):
            
            val = True
            for v in hashMap[u]:

                if color[v] != 0:
                    if color[v] == color[u]: 
                        return False  
                    
                else:
                    color[v] = -color[u] 
        
                    if not dfs(v):
                        return False

            return True
        
        for i in range(1, n+1):
            
            if not color[i]:
                color[i] = 1 
                answer = dfs(i)
                if not answer: 
                    
                    return False
                
                
        return True
