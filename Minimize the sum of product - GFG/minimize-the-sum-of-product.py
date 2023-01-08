#User function Template for python3

class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        # n = int(input())
        a.sort()
        b.sort()
        return (sum([a[i]*b[-1-i] for i in range(n)]))
        # return sum([a[i]*b[-1-i] for i in range(n)])



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minValue(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends