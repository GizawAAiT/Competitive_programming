class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["", 0]]
        for char in s:
            if char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                stack.pop()
            
        answer = ""
        for char, count in stack:
            answer += char*count
        
        return answer