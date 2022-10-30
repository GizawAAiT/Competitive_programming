class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        l, r, mx = 2*i + 1, 2*i +2, i
        if (r < n and arr[r] > arr[mx] ):
            mx = r
        if (l < n and arr[l] > arr[mx] ):
            mx = l
                                                                            
        if (i != mx):
            arr[mx], arr[i] = arr[i], arr[mx]
            self.heapify(arr, n, mx)
            
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2-1,-1,-1):
            self.heapify(self, arr, n, i)
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            self.heapify(arr, i, 0)