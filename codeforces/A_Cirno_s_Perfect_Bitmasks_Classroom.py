t = int(input())
for _ in range(t):
    x = int(input())
    y = 1
    while not x & y or not x ^ y:
        y += 1
    
    print(y)