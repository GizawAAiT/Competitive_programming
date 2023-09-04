class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr)==3: 
            return 1
        a, b = 0, len(arr)-1
        
        while a<b:
            m = (a+b)//2
            slope1 = arr[m]-arr[m-1]
            slope2 = arr[m+1]-arr[m]
            if slope1*slope2 < 0:
                return m
            if slope1 > 0:
                a = m
            else:
                b = m
