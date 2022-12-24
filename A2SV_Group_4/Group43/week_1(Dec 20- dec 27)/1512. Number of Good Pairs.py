class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        frequency = {}
        # build the frequency dictionary
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        
        visited = set()
        res = 0
        for n in nums:
            f = frequency[n]
            if f>1 and n not in visited:
                res += (f)*(f-1)/2
                visited.add(n)
        return int(res)