t = int(input())
for _ in range(t):
    n = int(input())
    s =  [int(_) for _ in input().split()]
    f =  [int(_) for _ in input().split()]
    s.insert(0, s[0])
    f.insert(0, s[0])
    answer = []
    for i in range(1, n+1):
        answer.append(f[i] - max(s[i], f[i-1]))
    print(*answer)