class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s)-1
        
        while s[right] == ' ': right -= 1
        left = right-1
        while left>-1 and s[left]!=' ': left-=1
        return right-left