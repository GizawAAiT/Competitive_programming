class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {n : ind for ind, n in enumerate(nums)}
        
        for n1, n2 in operations:
            nums[index[n1]] = n2
            index[n2] = index[n1]
            del index[n1]
        return nums
        
        
        
        
        