n, m, k = (int(_) for _ in input().split())
arr = [int(_) for _ in input().split()]
arr.sort()
n1 = (m//(k+1))
n2 = m-n1 
# print(n1,n2)
print(arr[-1]*n2 + arr[-2]*n1)