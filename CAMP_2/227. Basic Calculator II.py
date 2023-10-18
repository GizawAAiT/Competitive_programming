class Solution:
    def calculate(self, s: str) -> int:
        s += '+0'
        nums = []
        cur = 0
        op = '+'
        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                cur = cur *10 + int(c)

            elif op == '*':
                nums[-1] *= cur
                cur = 0

            elif op == '/':
                nums[-1] = floor(nums[-1]/cur ) if nums[-1]>= 0 else ceil(nums[-1]/cur)
                cur = 0

            elif op == '+':
                nums.append(cur)
                cur = 0

            elif op == '-':
                nums.append(-cur)
                cur = 0

            if c in ['+', '-', '*', '/']:
                op = c

        return sum(nums)