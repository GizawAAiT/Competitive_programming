class Solution:
    def minimumTotal(self, tr: List[List[int]]) -> int:
        Dp = [tr[-1]]
        for i in range(len(tr)-2,-1,-1):
            d = []
            for j in range(len(tr[i])):
                d.append(min(Dp[-1][j],Dp[-1][j+1])+tr[i][j])
            Dp.append(d)
        return Dp[-1][-1]