class Solution:
    def countOfAtoms(self, f: str) -> str:
        # if f[-1] == ')':
        #     f = f[1:-1]
        st, dic, elem, subscript, idx, cnt = [], defaultdict(int), '', 1, 0, 0
        for c in f[::-1]:
            if c.isdigit():
                cnt += int(c) * (10**idx)
                idx += 1
            elif c == ')':
                st.append(cnt)
                subscript *= cnt if cnt else 1
                idx = cnt = 0
            elif c == '(':
                divider = st.pop()
                subscript //= divider if divider != 0 else 1
                idx = cnt = 0
            elif c.isupper():
                elem += c
                dic[elem[::-1]] += (cnt or 1) * subscript
                elem, cnt, idx = '', 0, 0
            elif c.islower():
                elem += c

        return ''.join(k + str(v>1 and v or'') for k, v in sorted(dic.items()))

