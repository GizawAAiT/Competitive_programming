class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op, cl = n, n
        res, pat = [], ''

        def solve(op, cl, pat):
            if cl <= 0:
                res.append(pat)
                # pat = ''
                return 

            if op <= 0:
                pat += ')'
                solve(op, cl-1, pat)

            elif op == cl:
                pat += '('
                solve(op-1, cl, pat)

            else:
                solve(op-1, cl, pat+'(')
                solve(op, cl-1, pat+')')
            # print(pat)
        solve(n, n, '')
        return res
                




