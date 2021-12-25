class Solution: 
    def select(self, arr, i):
        pass
    
    def selectionSort(self, arr,n):
        #code here
        
        n=len(arr)
        for i in range(n-1):
            m=i
            for j in range(i+1,n):
                if(arr[j]<arr[m]):
                    arr[m],arr[j]=arr[j],arr[m]
                    