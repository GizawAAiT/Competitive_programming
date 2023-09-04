class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(n):
            result = 0
            while n>0:
                result += n&1
                n >>= 1
            return result
        print(count_ones(7))
        
        return ([count_ones(i) for i in range(n+1)] )