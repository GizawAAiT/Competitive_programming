q = int(input())
for _ in range(q):
    n = int(input())
    sides = [int(_) for _ in input().split()]
    sides.sort()
    left = 0
    right = len(sides)-1
    area = sides[left]*sides[right]
    flag = True
    for _ in range(n):
        if sides[left] != sides[left+1] or sides[right]!=sides[right-1]:
            flag = False 
            break
        if  sides[left]*sides[right] != area:
            flag = False 
            break

        left += 2
        right -= 2
    if flag:
        print('YES')
    else:
        print('NO')



