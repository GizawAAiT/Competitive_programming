class Solution:
    def longestCommonPrefix(self, s):
        res, i = '', 0
        while i<len(s[0]):
            cur = s[0][i]
            for word in s:
                if i>=len(word) or word[i]!=cur: return res
            res+= s[0][i]
            i+=1
        return res



            
