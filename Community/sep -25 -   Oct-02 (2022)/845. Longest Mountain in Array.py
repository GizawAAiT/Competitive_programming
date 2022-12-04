class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3: return 0
        res = 0
        def width(i,j):   
            res=0
            while j<len(arr) and arr[j]>arr[j-1]:
                j+=1
            if j==len(arr) or arr[j]==arr[j-1]: 
                return (j,j+1), 0
            while j<len(arr) and arr[j]<arr[j-1]:
                j+=1
            j-=1
            res = j-i+1
            i,j=j,j+1
            return (i,j),res
        i, j = 0, 1
        while j<len(arr):
            if arr[i]<arr[j]:
                (i,j) , r = width(i, j)
                res = max(r,res)
            else:
                i, j = i+1, j+1
        return res
                
                