t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(_) for _ in input().split()]

    arr.reverse()
    if arr[0] ==arr[-1]:
        print('NO')

    else:
        print('YES')
        i = 1
        while i<n and arr[0] == arr[i]:
            i+=1
        if i<n:
            arr[1],arr[i] = arr[i],arr[1]
    
        
        for x in arr:
            print(x,end=' ') 
        print()
