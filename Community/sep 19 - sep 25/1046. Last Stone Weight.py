class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def smash(s):
            if len(s)==1: return s
            s.sort()
            if s[-1]-s[-2]>0:
                s[-1]=s[-1]-s[-2]
                s.pop(-2)
            else: 
                s.pop()
                s.pop()
            return s
        while len(stones)>1:
            stones=smash(stones)
        return stones[0] if stones else 0