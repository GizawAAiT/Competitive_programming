for _ in range(int(input())):
    wt, et, ef = (int(_) for _ in input().split())
    print(min(4*wt, ef*wt + (4-ef)*et, ef*et + 4*et))