class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp=[[]]
        for e in nums:
            l=len(dp)
            for j in range(l):
                c=dp[j].copy()
                c.append(e)
                dp.append(c)
            
        return dp
        