class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        flips = []
        def flip(k):
            l, r = 0, k-1
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            flips.append(k)
        for i in range(len(arr)-1, 0, -1):
            k = i 
            for j in range(i, -1,-1):
                if arr[j]>arr[k]:
                    k=j
            flip(k+1)
            flip(i+1)

        return flips