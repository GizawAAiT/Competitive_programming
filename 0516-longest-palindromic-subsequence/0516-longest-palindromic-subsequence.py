class Solution(object):
    def longestPalindromeSubseq(self, s):
        d = {}
        def f(s):
            if s not in d:
                maxL = 0    
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
                d[s] = maxL
            return d[s]
        return f(s)