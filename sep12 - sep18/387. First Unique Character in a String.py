class Solution:
    def firstUniqChar(self, s: str) -> int:
        fr = {}
        for char in s:
            if char in fr.keys():
                fr[char] +=1
            else:
                fr[char] = 1       
        for i in range(len(s)):
            if fr[s[i]] ==1:return i
        return -1
                
            