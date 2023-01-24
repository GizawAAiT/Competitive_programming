n = int(input())
arr = [int(x) for x in input().split()]
neg, pos = [], []
i = 0
while i<len(arr) and not (neg and pos):
    if not neg and arr[i] <0: 
        neg.append(arr.pop(i))
    elif not pos and arr[i] > 0: 
        pos.append(arr.pop(i))
    
    else: i+=1
# print((((pos,neg,arr))))
i = 0
while not pos or (pos[0] < 0 and len(pos)==1):
    if arr[i]<0:
        pos.append(arr.pop(i))
        
    else: i+=1

print(1,end=' ')
for n in neg:
    print(n,end=' ')
print()

print(len(pos),end=' ')
for n in pos:
    print(n,end=' ')
print()

print(len(arr),end=' ')
for n in arr:
    print(n,end=' ')
