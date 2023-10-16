import heapq
from math import *
t = int(input())
for _ in range(t):
    n = int(input())
    arr =[int(_) for _ in input().split()]
    # arr.append(-0.5)
    # heapq.heapify(arr)
    arr.sort()
    answer = 0
    count = 1
    most_significant = ceil(log(arr.pop(), 2))
    
    while arr:
        top = arr.pop()
        # print(most_significant, top, "is the most sg bit")
        if ceil(log(top, 2)) == most_significant:
            count += 1
        else:
            answer += ((count)*(count -1))//2
            most_significant = ceil(log(top, 2))
            count = 1
    answer += ((count)*(count -1))//2
    print(answer)




    
