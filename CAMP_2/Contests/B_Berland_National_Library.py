n = int(input())
stack = set()
answer = 0
initial = 0
for _ in range(n):
    sign, val = input().split()
    if sign == "+":
        stack.add(val)
        answer = max(answer, len(stack))

    else:
        if val in stack:
            stack.remove(val)
        else:
            answer += 1
print(answer + initial)
    