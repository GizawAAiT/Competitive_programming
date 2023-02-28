class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         for i in range(1,len(nums)):
#             nums[i] += nums[i-1]
        
        nums.insert(0,0)
        
        d = defaultdict(int)
        d[0] = 1
        result = 0
        for i  in range(1,len(nums)):
            nums[i] += nums[i-1]
            if nums[i]%k in d:
                result += d[nums[i]%k ]
            d[nums[i]%k ] += 1
        return result