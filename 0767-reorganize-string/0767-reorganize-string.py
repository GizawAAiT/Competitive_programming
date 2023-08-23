class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key)) #Min heap.
        
        ans = ''
        top = heapq.heappop(heap)
        while heap:
            ans += top[1]
            elem = heapq.heappop(heap)
            if top[0] < -1:
                heapq.heappush(heap, (top[0]+1, top[1]))
            top = elem
            # print(heap)
        if top[0] < -1 :
            return ""
        return ans + top[1]
            