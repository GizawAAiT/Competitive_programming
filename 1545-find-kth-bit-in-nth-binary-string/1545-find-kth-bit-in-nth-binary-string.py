class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def nthSequence(n):
            if n == 1:
                return '0'
            prev = nthSequence(n-1)
            prev += '1'
            for i in range(len(prev)-2, -1, -1):
                prev += '1' if prev[i] =='0' else '0'
            # print(prev)
            return prev
        
        return nthSequence(n)[k-1]
    
    