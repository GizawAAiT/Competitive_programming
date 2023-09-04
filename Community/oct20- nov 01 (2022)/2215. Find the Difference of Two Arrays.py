class Solution:
    def findDifference(self, n1: List[int], n2: List[int]) -> List[List[int]]:
        n1, n2 = set(n1), set(n2)
        
        res = [[],[]]
        for n in n1:
            if n not in n2:
                res[0].append(n)
        for n in n2:
            if n not in n1:
                res[1].append(n)
        return res