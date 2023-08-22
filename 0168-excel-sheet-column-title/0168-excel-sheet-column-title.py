class Solution:
    def convertToTitle(self, colNumber: int) -> str:
        result = ''
        while colNumber>0:
            cur, colNumber = colNumber%26, colNumber//26
            print((cur, colNumber))
            if not cur: 
                cur = 26
                colNumber -= 1
            result = chr(64+cur) + result
        return result
            
            
            