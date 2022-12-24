class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        def manhattan(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        d = inf
        p = -1
        i = 0
        while i < len(points):
            if x == points[i][0] or y == points[i][1]:
                di = manhattan((x,y),points[i]) 
                if di < d:
                    d = di
                    p = i
            i+=1
        return p
        