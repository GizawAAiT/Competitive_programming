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
    n, k = inlt()
    s = input()
    left = ans = 0
    count_a, count_b = 0, 0
    for right in range(n):
        if s[right] == "a":
            count_a += 1
        else:
            count_b += 1
        while min(count_a, count_b) > k:
            if s[left] == "a":
                count_a -= 1
            else:
                count_b -= 1 
            left += 1
        ans = max(ans, right-left + 1)
    print(ans)
main()