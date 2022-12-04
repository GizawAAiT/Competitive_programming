class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      
        count, total = 0, 0
        dict = {0:1}
        for i in nums:
            total += i
            
            if dict.get(total-k):
                
                count += dict[total-k]   
                
            if dict.get(total):                
                dict[total] += 1                
            else:
                dict[total] = 1
        return count