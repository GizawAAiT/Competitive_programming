class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(i):
            
            if len(path) == k:
                result.append(path[:])
                return
            
            for num in range(i, n+1): 
                
                path.append(num)
                backtrack(num+1)
                path.pop() 
        backtrack(1)
        return result