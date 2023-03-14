t = int(input())

for i in range(t):
    math, pro = map(int, input().split())
    print(min(min(pro, math), (pro+math)//4))
    # low, high = 0, (pro+math)//4
    # minority = min(math, pro)
    # answer = 0
    # while low <= high:
    #     mid = low + (high-low)//2
       
    #     if mid>minority:
    #         high = mid - 1
    #     else:
    #         low = mid + 1
    
    # print(high)

