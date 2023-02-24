class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{":"}", "[":']', "(":")"}
        
        stack = []
        for c in s:
            if c in pairs.keys():
                stack.append(c)
            elif  stack and pairs[stack[-1]] == c:
                stack.pop()
            else: return False
        return not stack