class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True]*(n)
        prime[0]= prime[1] = False
        for i in range(2, n):
            if prime[i]:
                temp = 2*i
                while temp<n:
                    prime[temp] = False
                    temp += i
        return sum(prime)