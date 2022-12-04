class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        res = 0
        
        for i in range(len(arr)-2):
            j, k, T = i+1, len(arr)-1, target - arr[i]
            
            while j<k:
                # print((i,j,k))
                if arr[j]+arr[k]>T: k-=1
                elif arr[j]+arr[k]<T: j+=1
                elif arr[j]!=arr[k]:
                    l, r = 1, 1
                    j, k = j+1, k-1
                    
                    while j<k+1 and arr[j]==arr[j-1]:
                        l, j = l+1, j+1 
                        
                    while j<k+1 and arr[k]==arr[k+1]:
                        r, k = r+1, k-1
                  
                    res += l*r 
                else:
                    res += (k-j+1)*(k-j)//2
                    break
                # print((i,j,k),"=>",T)
        return res%(10**9 + 7)
            
                        
                    