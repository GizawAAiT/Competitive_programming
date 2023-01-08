#User function Template for python3
from collections import Counter
class Solution:
    def countPairs (self, n, arr, k):
        # code here
        arr = [a%k for a in arr]
        c = Counter(arr)
        return int(sum([(c[i]/2)*(c[i]-1) for i in c]))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        k=int(input())
        
        ob = Solution()
        print(ob.countPairs(n,arr,k))
# } Driver Code Ends