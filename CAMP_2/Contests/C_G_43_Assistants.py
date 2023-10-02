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


def main():
    for _ in range(inp()):
        n = int(inp())
        pref = defaultdict(int)
        m = 100
        for _ in range(n):
            start, end = invr()
            pref[start] += 1
            pref[end] -= 1
            m = max(m, end)
        
        maxPref = pref[0]
        for i in range(1, m + 1 ):
            pref[i] += pref[i-1]
            maxPref = max(maxPref, pref[i])
        print(maxPref)
main()

        



