class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -inf
        
        cur_sum = 0
        for n in nums:
            
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum