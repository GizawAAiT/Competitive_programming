t = int(input())
def minim(s):
    if s < 10:
        return s
    res = []
    largest = 9
    while s>0:
        if s < largest:
            res.append(s)
            break
        res.append(largest) 
        s -= largest
        largest -= 1
    return int(''.join([str(n) for n in reversed(res)]))

for _ in range(t):
    s = int(input())
    
    print(minim(s))

