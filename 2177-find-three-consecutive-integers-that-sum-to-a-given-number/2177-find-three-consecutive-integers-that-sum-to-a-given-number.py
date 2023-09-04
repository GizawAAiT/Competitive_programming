class Solution:
    def sumOfThree(self, n: int) -> List[int]:
        if not n%3: 
            n = n//3
            return [n-1, n, n+1]
        else: return []