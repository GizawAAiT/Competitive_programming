class Solution:
    def checkStraightLine(self, coor: List[List[int]]) -> bool:
        if len(coor) <=2:
            return True
        x0,y0,x1,y1 = coor[0][0],coor[0][1], coor[1][0],coor[1][1]
        dx,dy = x1-x0, y1-y0
        
        for p in coor[2:]:
            x,y = p[0],p[1]
            if (x-x1)*dy != (y-y1)*dx:
                return False
        return True
