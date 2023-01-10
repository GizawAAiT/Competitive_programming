class Solution:
    def sumOfThree(self, n: int) -> List[int]:
        if not n%3: 
            return [n//3 -1, n//3, n//3 +1]
        else: return []