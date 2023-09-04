class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        
        if len(arr) < 3:
            return True
        d = arr[1]-arr[0]
        
        i = 2
        while i < len(arr):
            if arr[i]-arr[i-1] !=d:
                return False
            i+=1
        return True