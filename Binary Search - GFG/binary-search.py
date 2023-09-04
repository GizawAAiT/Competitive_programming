#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		i, j = -1, n
		while i<j-1:
		    m = (i+j)//2
		    if arr[m] == k: return m
		    if k < arr[m]: j = m
		    else: i = m
	    return -1
	    
		        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends