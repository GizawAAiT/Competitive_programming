class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        piv, binary = -1, [0 for _ in range(len(flips))]
        res = 0
        for inx in range(len(flips)):
            i = flips[inx]
            binary[i-1]=1
            while piv<len(binary)-1 and binary[piv+1]==1: piv+=1
            
            if inx == piv: 
                res +=1
                
        return res