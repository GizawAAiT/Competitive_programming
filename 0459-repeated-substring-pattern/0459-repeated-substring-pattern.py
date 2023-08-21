class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2: return False
        def get_primes(n):
            p = set()
            for i in range(2,n//2 + 1):
                if n % i == 0:
                    p.add(i)
                    
            p.add(n)
            return p
        
        def is_correct(prime):
            step = len(s) // prime
            sub_str = s[:step]
            for i in range(0, len(s), step):
                # print((i, step))
                if sub_str != s[i:i+step]:
                    return False
            return True
                
        primes = get_primes(len(s))
        # print(primes)
        for prime in primes:
            if is_correct(prime):
                return True
        return False
        