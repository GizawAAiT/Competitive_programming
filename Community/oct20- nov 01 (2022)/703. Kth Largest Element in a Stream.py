class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)
        
        print(f" heapq = {self.minHeap},{nums}")
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
    def add(self, v: int) -> int:
        heapq.heappush(self.minHeap, v) 
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    # self.__init__()

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)