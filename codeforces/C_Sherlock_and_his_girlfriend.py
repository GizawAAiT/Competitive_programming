from collections import defaultdict
def isPrime(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

primes = []
n = int(input())

for i in range(2, n+2):
    if isPrime(i):
        primes.append(i)



comp = []
for i in range(2, n+2):
    if i not in primes:
        comp.append(i)

answer = [1 if isPrime(x) else 2 for x in range(2, n+2)]
if n == 1:
    print(1)
    print(1)
else:
    print(1 + int(len(comp)>0))
    print(*answer)