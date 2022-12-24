# Enter your code here. Read input from STDIN. Print output to STDOUT
A = input().split()
n = int(input())

i = 0
vis = set()
while i<n:
    s = input().split()
    for elem in s:
        if elem not in A:
            print('False')
            i=n
            break
        else:
            vis.add(elem)
    i+=1
if i == n and len(A) > len(vis):
    print('True')
         