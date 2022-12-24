# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
english = set(input().split())
f = int(input())
franch = set(input().split())
print(len(english.union(franch)))