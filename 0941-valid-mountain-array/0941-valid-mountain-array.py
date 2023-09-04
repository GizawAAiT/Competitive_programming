class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3 or arr[1] <= arr[0]: return False
        
        i = 1
        while i<len(arr) and arr[i]>arr[i-1]: i+=1
        while i<len(arr) and arr[i]<arr[i-1]: i+=1
        return i==len(arr) and arr[-1]<arr[-2]