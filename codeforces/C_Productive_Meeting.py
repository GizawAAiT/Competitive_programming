import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(a) for a in input().split()]
    heap = []
    for index in range(n):
        if arr[index] > 0:
            heap.append([-arr[index], index + 1])

    heapq.heapify(heap)
    result = []
    while len(heap) > 1:
        s_a, a = heapq.heappop(heap)
        s_b, b = heapq.heappop(heap)
        
        result.append([a, b])
        s_a += 1
        s_b += 1

        if s_a < 0:
            heapq.heappush(heap, [s_a, a])

        if s_b < 0:
            heapq.heappush(heap, [s_b, b])
    
    print(len(result))
    for pair in result:
        print(*pair)
                
