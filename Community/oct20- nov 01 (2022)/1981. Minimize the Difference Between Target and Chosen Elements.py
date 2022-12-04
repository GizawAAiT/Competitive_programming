class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        cache = set(mat.pop())
        
        while mat:
            a = mat.pop()
            cur = cache.copy()
            cache.clear()
            
            while a:
                v1 = a.pop()
                for c in cur:
                    cache.add(c+v1)
        res = 2**32 
        print(cache)
        for c in cache:
            res = min(res, abs(target-c))
        return res