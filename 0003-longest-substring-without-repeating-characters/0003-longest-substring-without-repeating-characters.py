class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = length = 0
        
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            length = max(right-left+1, length)
        return length