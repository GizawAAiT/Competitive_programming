class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res = 0
        while tokens:
            if power >= tokens[0]:
                power-=tokens.pop(0)
                res+=1
            elif res>=1 and power+tokens[-1] > tokens[0] and len(tokens)>1:
                power+=tokens.pop()
                res-=1
            else: break
                
        return res