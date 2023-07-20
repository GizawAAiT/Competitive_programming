n, c = (int(_) for _ in input().split())
t = [int(_) for _ in input().split()]

remain_words = 1
for i in range(n-1):
    if t[i+1] - t[i] > c:
        remain_words = 1
    else:
        remain_words += 1
    
print(remain_words)