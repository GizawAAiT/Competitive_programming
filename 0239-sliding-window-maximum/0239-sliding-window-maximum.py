class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        dictionary = defaultdict(int)
        left = 0
        result = []
        for right in range(len(nums)):
            if dictionary[nums[right]] == 0:
                heapq.heappush(heap, -nums[right]) #Add to the heap
            dictionary[nums[right]] += 1
            
            if right - left == k-1:
                while heap:
                    elem = -heapq.heappop(heap)
                    if dictionary[elem] > 0: #If count is not zero
                        result.append(elem)
                        heapq.heappush(heap, -elem) #push it back to the heap.
                        break
                dictionary[nums[left]] -= 1
                left += 1
            
        return result
        
                        
                        
                        