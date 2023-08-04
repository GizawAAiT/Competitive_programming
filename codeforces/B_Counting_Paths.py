
T = int(input())
for _ in range(T):
    # res = 0
    memo = {}
    def backtrack(a, b, alt, depth):
        # global res
        if b-alt > a-depth:
            return 0

        if depth == a:
            # res += int(alt == b)
            return int(alt == b)
        
        if alt == b:
            return 1

        if ((alt, depth) not in memo ):
            left = backtrack(a, b, alt, depth + 1) % (10**9 + 7)
            right = backtrack(a, b, alt+1, depth + 1) % (10**9 + 7)
            memo[(alt, depth)] = (left + right) % (10**9 + 7)

        return memo[(alt, depth)]

    a, b = (int(_) for _ in input().split())
    

    ans = 2 * backtrack(a, b, 0, 1) 

    print(ans % ((10**9) + 7))



