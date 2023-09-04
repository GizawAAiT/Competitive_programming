class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        i = 0
        while i<len(s):
            if not s[i].isalnum(): s.pop(i) 
            else: i+=1
        for i in range(len(s)//2):
            if s[i] != s[-i-1]: return False
        return True