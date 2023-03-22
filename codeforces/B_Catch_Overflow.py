l = int(input())
stack = []
for _ in range(l):
    com  = input().split(' ')
    
    if com[0] == 'add':
        if stack and len(stack[-1]) == 1: 
            stack[-1][0] += 1 
        else:
            stack.append([1])
    elif com[0] == 'for':
        stack.append(com)
    else:
        if len(stack[-1]) == 1: 
            while len(stack) >1 and  len(stack[-2])==1:
                stack[-2][0] += stack[-1][0]
                stack.pop()
            stack[-2] = [stack[-1][0] * int(stack[-2][1])]
        stack.pop()  
    # print(stack)
sum_ = sum(stack[i][0] for i in range(len(stack)))
if sum_ > (2**32)-1:
    print('OVERFLOW!!!') 
else:
    print(sum_)
            


