class Solution:
    def toLowerCase(self, s: str) -> str:
        s=list(s)
        for c in range(len(s)):
            if s[c].isupper(): s[c]=s[c].lower()
        return "".join(s)