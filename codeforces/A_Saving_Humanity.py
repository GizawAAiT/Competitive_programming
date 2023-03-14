t = int(input())
for i in range(t):
    n, m  = (int(_) for _ in input().split())
    s = list(input())


    left  = 0
    while left < n and s[left]=='0':
        left +=1
    left_most  = left
    
    for right in range(left , n):
        if (left == right or left==right-1) and s[right] == '1':
            left = right
        elif s[right] =='1':
            c = m
            l,r = left+1, right-1
            while l<r and c>0:
                c-=1
                s[l] = '1'
                s[r] = '1'
                l+=1
                r-=1
            left=right
    right_most = left
    
    if left_most<n and s[left_most]=='1':
        left_most-=1
        c = m
        while left_most >=0 and c>0:
            c-=1
            s[left_most] = '1'
            left_most-=1
    if right_most<n and s[right_most]=='1':
        right_most +=1
        c = m
        while right_most <n  and c>0:
            c-=1
            s[right_most] = '1'
            right_most+=1
    print(''.join(s)) 




    
        
    



