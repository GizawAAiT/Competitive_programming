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

    n = inp()
    row1 = inlt()
    row2 = inlt()
    grid = [row1, row2]

    memo = [[None for _ in range(n+1)] for _ in range(2) ]
    def recur(turn, indx, n):
        if indx >= n:
            return 0
       
        if memo[(turn +1)%2][indx+1] ==  None:
            # print((turn +1)%2, indx+1)
            memo[(turn +1)%2][indx+1] = recur((turn +1)%2, indx+1, n)
        if memo[turn][indx+1] == None:
            memo[turn][indx+1] = recur(turn, indx+1, n)

        return max(grid[turn][indx] + memo[(turn +1)%2][indx+1], memo[turn][indx+1])
    
    answer = max(recur(0, 0, n), recur(1, 0, n))
    print(answer)  


main()