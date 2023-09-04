class Solution:
    def calPoints(self, op: List[str]) -> int:
        sc = [int(op.pop(0))]
        while op:
            s = op.pop(0)
            if s == '+':
                sc.append(int(sc[-1]) + int(sc[-2]))
            elif s == 'D':
                sc.append(2*int(sc[-1]))
            elif s == "C":
                sc.pop()
            else:
                sc.append(int(s))
        print(sc)
        return sum(sc) 
