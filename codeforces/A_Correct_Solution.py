import heapq
n = input()
m = input()
digits = [int(i) for i in n]
heapq.heapify(digits)
result = []

while digits:
    result.append(heapq.heappop(digits))

if len(result) > 1 and result[0] == 0:
    j = 1
    while result[j] == 0:
        j += 1
    
    result[j], result[0] = result[0], result[j]

print("OK" if m == ''.join(str(i) for i in result) else "WRONG_ANSWER")
