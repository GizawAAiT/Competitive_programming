n = int(input())
count = 0
for _ in range(n):
    count += sum([int(_) for _ in input().split()])
print(count // 2)
