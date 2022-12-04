class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr=sorted(arr)
        m=0
        while m<len(arr) and arr[m]<0: 
            m+=1
        arr,arrneg=arr[m:],arr[:m]
        
        for i in range(len(arr)):
            j = len(arr) -1
            while j>i and 2*arr[i]<arr[j]: 
                j-=1
            if 2*arr[i]==arr[j] and i!=j: return True
        
        
        arrneg=list(reversed([-arrneg[i] for i in range(len(arrneg))])) 
        print("fuck:",arrneg)
        for i in range(len(arrneg)):
            j = len(arrneg) -1
            while j>i and 2*arrneg[i]<arrneg[j]: 
                j-=1
            if 2*arrneg[i]==arrneg[j] and i!=j: return True
        return False
                       