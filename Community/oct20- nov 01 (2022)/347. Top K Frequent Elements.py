class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heapq.heapify(nums)
        f = {}  #frequencies dictionary.
        for n in nums:
            if n in f:
                f[n] +=1
            else: f[n] = 1
        
        ans = []
        for i in f:
            heapq.heappush(ans,(f[i],i))
            if len(ans)>k: 
                heapq.heappop(ans)
        return [i[1] for i in ans] 
           