t = int(input())
for _ in range(t):
    n = int(input())
    d = 0
    zero, one = 0, 0
    while n and not one:
        cur = n & 1
        n >>= 1

        if cur == 0 and not zero:
            zero = 2 ** d

        if cur == 1 and not one:
            one = 2 ** d
        d += 1

    

    if not n and not zero:
        zero = 2 ** d

    print(zero + one)
