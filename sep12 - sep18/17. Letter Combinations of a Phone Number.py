class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}        
        num = list(digits)
        arr = [d[i] for i in num]
        
        A = list(arr.pop(0))
        while arr:
            B = list(arr.pop(0))
            A = self.comb(A,B)
        return A
    def comb(self,l,m):
        combination = []
        for a in l:
            for b in m:
                combination.append((a+b))
        return combination
