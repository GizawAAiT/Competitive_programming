class Solution:
    def goodDaysToRobBank(self, s: List[int], t: int) -> List[int]:
        N = len(s)
        l, r = 0, -1
        left =  [0]
        for i in range(1, len(s)):
            if s[i] <= s[i-1]:
                l += 1
            else: l = 0
            left.append(l)
            
        res = []
        for i in range(N-1, t-1, -1):
            if r ==-1 or s[i] <= s[i+1]:  
                r += 1
            else: r = 0
            if left[i] >= t and r >= t:
                res.append(i)
        return res
        