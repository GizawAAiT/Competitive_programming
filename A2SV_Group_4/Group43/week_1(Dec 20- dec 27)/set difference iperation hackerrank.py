# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
english = input().split()
f = int(input())
franch = input().split()

count = 0
for en in english:
    count += int(en not in franch)
print(count)