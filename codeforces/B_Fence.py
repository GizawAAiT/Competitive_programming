n, k = (int(_) for  _ in input().split())

h = [int(_) for  _ in input().split()]

total = cur = sum(h[:k])
left = 0
answer = 0

for right in range(k, len(h)):
    cur +=h[right] - h[left] 
    left += 1
    right += 1
    if cur < total:
        total = cur
        answer = left
    
print(answer + 1)