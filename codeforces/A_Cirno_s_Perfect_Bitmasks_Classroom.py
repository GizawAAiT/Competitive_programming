t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(3)
    
    else:
        i = 0
        while not n & 1:
            n >>= 1 
            i += 1
        
        print(2**i + 1 if not n>>1 else 2**i)

