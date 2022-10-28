class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        req = abs(sum(nums)-goal)
        
        return ceil(req/limit)