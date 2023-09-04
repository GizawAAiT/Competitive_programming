class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<11: return 
        
        catche=set()
        res=set()
        for i in range(len(s)-9):
            if s[i:i+10] in catche:
                res.add(s[i:i+10])
            else:
                catche.add(s[i:i+10])
        return res
                