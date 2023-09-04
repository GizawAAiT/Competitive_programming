class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        s = 0
        for gd in grid:
            while gd and  gd[-1] < 0:
                s+=1
                gd.pop()
        return s