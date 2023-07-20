from math import *
n = int(input())
m = int(input())

total, maximum = 0, float('-inf')
for _ in range(n):
    x = int(input())
    maximum = max(maximum, x)
    total += x

minimum = max(maximum, ceil((total + m)/ n))
maximum += m
print(minimum, maximum)
