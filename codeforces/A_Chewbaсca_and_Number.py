x = []
num = int(input())

while num>0:
    x.append(num%10)
    num //=10
x.reverse()
# print(x)
for i in range(1,  len(x)):
    if x[i] > 4:
        x[i] = 9-x[i]
if x[0] >4 and x[0]!=9:
    x[0] = 9-x[0]
print(''.join(str(_) for _ in x))
# left = 0
# while left < len(x) and x[left] ==0:
#     left += 1
# if left == len(x):
#     print(9-x[-1])
# else: 
#     print (int(''.join(str(_) for _ in x)))