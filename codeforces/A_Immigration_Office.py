n = int(input())
names = input().split()
q = int(input())

for i in range(q):
    name = input()
    left = -1
    right = len(names)
    while left<right-1:
        mid = (left+right)//2
        if names[mid] < name:
            left = mid
        else:   
            right = mid
    print(right)
