class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        ans = 1
        Q = {s[0]}
        i,j = 0,1
        while j<len(s):
            if s[j] in Q:
                if ans<j-i: 
                    ans = j-i
                while s[j] in Q:
                    Q.remove(s[i])
                    i+=1
            Q.add(s[j])
            j+=1
        if ans<j-i:
            ans = j-i
        return ans