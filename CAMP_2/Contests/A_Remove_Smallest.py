from collections import defaultdict
from sys import stdin, stdout


def inp():
    return int(stdin.readline())


def inlt():
    return list(map(int, stdin.readline().strip().split()))


def insr():
    s = stdin.readline().strip()
    return list(s[:len(s)])


def invr():
    return map(int, stdin.readline().strip().split())


def solve(arr, n):
    for i in range(1,n) :
        if arr[i] > arr[i-1] +1: return "NO"
    return "YES"

t = inp()
for _ in range(t):
    n = inp()
    arr = inlt()
    arr.sort()
    print(solve(arr, n))

