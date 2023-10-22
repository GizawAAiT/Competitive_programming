n, lowerLimit, upperLimit, x = (int(_) for _ in input().split())
c = [int(_) for _ in input().split()]
c.sort()

# do the cummulative
for i in range(1, n):
    c[i] += c[i-1]
c.insert(0, 0)
answer = 0
print(c)
left = 1
while left < n:
    l, r = left, n+1
    right1 = right2 = float('inf')
    while l<r-1:
        # print('x:', x, "ll:", lowerLimit)
        mid = l+(r-l)//2
        if c[mid]-c[left-1] >= x and c[mid]-c[left-1] >= lowerLimit:
            r = mid
            print(l,r, "= l,r")
            print('cum:', (c[mid]-c[left-1]))
        else:
            l = mid
            print("l, r", (l, r))
            print('cum:', c[mid]-c[left-1])
    right1 = r
    
    l, r = left, n+1
    while l<r-1:
        mid = l+(r-l)//2
        if c[mid]-c[left-1] < upperLimit:
            l = mid
        else:
            r = mid
    right2 = l 
    if right1 != float('inf') and right2 != float('inf'):
        answer += max(right2-right1 + 1, 0)
        print(right1, right2, "with left = ", left)
    left += 1

print(answer)

    




