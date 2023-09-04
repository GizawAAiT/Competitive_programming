# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
nums = input().split()
A = set(input().split())
B = set(input().split())


h = 0
for num in nums:
    h += (int(num in A) - int(num in B))
print(h)
