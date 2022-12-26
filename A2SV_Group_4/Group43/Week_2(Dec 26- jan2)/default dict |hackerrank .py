# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = [int(i) for i in input().split()]
A = defaultdict(list)

for i in range(n):
    A[input()].append(str(i+1)) 
for _ in range(m):
    w = input()
    if w in A:
        print(' '.join(A[w]))
    else:
        print('-1')
