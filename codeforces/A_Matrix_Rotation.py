t = int(input())
for _ in range(t):
    val = 'NO'
    arr = [int(_) for _ in input().split()]
    for i in input().split():
        arr.append(int(i))
    
    arr[-1],arr[-2]=arr[-2],arr[-1]
    for i in range(4):
        if arr[i%4]<arr[(i+1)%4] and arr[(i+3)%4]<arr[(i+2)%4] and  arr[(i)%4]<arr[(i+3)%4] and arr[(i+1)%4]<arr[(i+2)%4]:
            val = 'YES'
            break
    print(val)
    

    