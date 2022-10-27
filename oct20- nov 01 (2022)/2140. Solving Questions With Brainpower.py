class Solution:
    def mostPoints(self, ques: List[List[int]]) -> int:
        n = (len(ques))
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1): 
            p, esc = ques[i]  
            dp[i] = max(p + dp[min(esc+i+1,n)], dp[i+1] )  
        return dp[0]  
    