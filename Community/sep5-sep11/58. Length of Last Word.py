class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = b = len(s)-1
        
        while b > 0 and s[b] == " ":
            b-=1
        a=b
        while a > 0 and s[a] != " ":
            a-=1
        if a ==0 and s[a]!=" ":
            a-=1
        return (b-a)