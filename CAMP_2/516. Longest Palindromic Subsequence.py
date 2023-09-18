class Solution:
    
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def recur(left, right, length):
            if left > right:
                return 0
            
            if left == right:
                return 1
            
            if (left+1, right) not in memo:
                memo[(left+1, right)] = recur(left+1, right, length)
            
            t = right
            while t>left and s[t]!=s[left]:
                t -= 1
                
            if (left, right) not in memo:
                memo[(left, right)] = recur(left+1, t-1, length) + (2 if left < t else 1)
            
            return max(memo[(left+1, right)], memo[(left, right)])
        
        return recur(0, len(s)-1, 0) 