#User function Template for python3

class Solution: 
    def select(self, arr, i, n):
        # code here 
        r = i
        while i<n:
            if arr[i] < arr[r]: 
                r = i
            i+=1
        return r
            
    def selectionSort(self, arr,n):
        #code here
        for _ in range(n-1):
            r = self.select(arr, _, n)
            arr[_], arr[r] = arr[r], arr[_]
        return arr
