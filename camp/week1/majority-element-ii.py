class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # heap sort approach
        frequencies = Counter(nums)
        
        # Obtains top 2 (because we are looking for n / 3)
        top2 = heapq.nlargest(2, frequencies, key=frequencies.get)
        
        # Filtering
        threshold = n / 3
        results = list(filter(lambda element: frequencies[element] > threshold, top2))
        
        return results
        