t = int(input())
for _ in range(t):
    c, b, a = sorted(int(_) for _ in input().split())
    # if a < b:
    #     a, b = b, a
    # if b < c:
    answer = 0
    if a :
        a-=1
        answer += 1
    if b :
        b-=1
        answer += 1
    if c:
        answer += 1
        c -=1
    if a and b:
        answer += 1
        a -= 1
        b -= 1
    if a and c:
        answer += 1
        a -= 1
        c -= 1
    
    if b and c:
        answer += 1
        b -= 1
        c -= 1
    if a and b and c:
        answer += 1
        # a -= 1
        # b -= 1
        # c -= 1
    print(answer)