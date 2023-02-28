class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        nums.insert(0,0)
        
        d = defaultdict(int)
        
        result = 0
        for n in nums:
            if n%k in d:
                result += d[n%k]
            d[n%k] += 1
        return result