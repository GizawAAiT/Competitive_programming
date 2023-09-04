class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score_stack = [0]
        for par in s:
            if par =='(':
                score_stack.append(0)
            else:
                cur_score = score_stack.pop()
                score_stack[-1] += max(1, cur_score*2)
        return score_stack[0]