from math import *
from collections import defaultdict
def primeFactors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n = n // 2
    for i in range(3,int(sqrt(n))+1,2):
        while n % i== 0:
            factors.add(i)
            n = n // i
    if n >2:
        factors.add(n)       
    return factors

k, n = (int(_) for _ in input().split())
arr = [int(_) for _ in input().split()]

prod = defaultdict(int)
total = 0
answer = 0
for indx, num in enumerate(arr):
    total += num
    for p in primeFactors(num):
        prod[p] += num
    val = k + max(prod.values())-total if len(prod) >0 else k-total
    if val >= 0:
        answer = indx+1
    else:
        break
print(answer)
    


    

         