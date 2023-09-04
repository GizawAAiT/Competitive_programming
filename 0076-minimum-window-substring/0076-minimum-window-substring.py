from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = Counter(t)
        k = len(dt)
        left = 0
        dw = defaultdict(int)
        res = (0, float('inf')) 
        for right in range(len(s)):
            dw[s[right]] += 1
            if dw[s[right]] == dt[s[right]]:
                k-=1
                
            while k == 0 and dw[s[left]] > dt[s[left]]:
                dw[s[left]] -= 1
                left += 1
                
            if k ==0 and right-left < res[1]-res[0]:
                res = (left, right)
                
        
        if res == (0, float('inf')):
            return ''
        return s[res[0]:res[1]+1]