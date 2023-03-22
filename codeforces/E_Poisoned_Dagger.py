for _ in range(int(input())):
    n, h = (int(_) for _ in input().split())
    a = [int(_) for _ in input().split()]
    def attack(k):
        total = 0
        for i in range(len(a)-1):
            total += min((a[i+1]-a[i]), k)
        return total + k

    left = 0
    right = h+1

    while left < right-1:
        mid = left + (right-left)//2
        if attack(mid) < h:
            left = mid
        else:
            right = mid

    print(right)

    
