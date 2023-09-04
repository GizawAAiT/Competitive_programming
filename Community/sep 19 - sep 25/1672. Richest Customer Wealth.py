class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for cus in accounts:
            mx = max(mx, sum(cus)) 
        return mx