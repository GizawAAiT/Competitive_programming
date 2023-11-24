class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # floid warshal

        ratio = defaultdict(float)
        variables = set()
        for i in range(len(equations)):
            a, b = equations[i]
            ratio[(a, b)] = values[i]
            if values[i] != 0:
                ratio[(b, a)] = 1/values[i] 
            variables.add(a)
            variables.add(b)
        
        variables = list(variables)

        for mid in variables:
            for a in variables:

                for b in variables:
                    if (a, mid) in ratio and (mid, b) in ratio:
                        ratio[(a, b)] = ratio[(a, mid)] * ratio[(mid, b)]
        
        res = []
        for q in queries:
            res.append(ratio[tuple(q)] if tuple(q) in ratio else -1)
        return res
        
        