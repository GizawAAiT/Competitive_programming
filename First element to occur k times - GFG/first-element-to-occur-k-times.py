#User function Template for python3

from collections import defaultdict
class Solution:
    def firstElementKTime(self,  a, n, k):
        
        count = defaultdict(int)
        for char in a:
            count[char] += 1
            if count[char]>= k: return char
        return -1
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends