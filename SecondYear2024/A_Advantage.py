def advantage(participants):
    a, b = 0, 0
    for p in participants :
        if p > a:
            b, a = a, p
        elif p > b:
            b = p
    
    return [p-a if p-a != 0 else a-b for p  in participants]

for _ in range(int(input())):
    n = int(input())
    participants = [int(_) for _ in input().split()]
    print(*advantage(participants))
