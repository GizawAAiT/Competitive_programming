from collections import defaultdict
from sys import stdin, stdout
import heapq

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
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(_) for _ in input().split()]
        arr = [(-arr[i], i+1) for i in range(n)]
        answer = []
        heapq.heapify(arr)
        while len(arr) > 1:
            p1, i1 = heapq.heappop(arr) 
            p2, i2 = heapq.heappop(arr)
            
            if p1 <= -1 and p2 <= -1:
                answer.append((i1, i2))
                p1 += 1
                p2 += 1
            if p1 <0 :
                heapq.heappush(arr, (p1, i1))
            if p2 <0:
                heapq.heappush(arr, (p2, i2))
        
        print(len(answer))
        for ans in answer:
            print(ans[0], ans[1])

main()
