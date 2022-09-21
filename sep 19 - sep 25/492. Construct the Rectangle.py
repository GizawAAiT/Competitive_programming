class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = floor(sqrt(area))
        while w>=0:
            if area/w==area//w: break
            w-=1
        
        return [area//w,w]        