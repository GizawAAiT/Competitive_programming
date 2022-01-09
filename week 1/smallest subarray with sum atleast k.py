class Solution:
    def shortestSubarray(self, n, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
       
        dp = [0] * (len(n) + 1)

        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + n[i - 1]

        res = len(n) + 1
        
        Q = collections.deque()

        for i in range(len(dp)):
            while Q and dp[i] - dp[Q[0]] >= K:
                res = min(res, i - Q.popleft())
            while Q and dp[i] < dp[Q[-1]]:
                Q.pop() # pop right
            Q.append(i)
        if res == len(n)+1:
            return -1
        return res 