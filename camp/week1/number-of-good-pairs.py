class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        result = 0
        for n in nums:
            result += count[n]
            count[n] += 1
        
        return result
