class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i, j = 1, 0
        res, methods = [], []
        while i<=n:
            res.append(i)
            methods.append('Push')
            if res[-1] != target[j]:
                res.pop()
                methods.append('Pop')
            else: 
                j+=1
                # methods.append('Push')
            if res and res[-1]==target[-1]: return methods
            i+=1
                
            