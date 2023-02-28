class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        d = defaultdict(int)
        nums.insert(0,0)
        
        result = 0
        for n in nums:
            if n-k in d:
                result += d[n-k]
            d[n] += 1
        return result