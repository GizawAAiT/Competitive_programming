class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        color1 =image[sr][sc]
        if color == color1:
            return image
        def fill(r, c):
            if (r<0 or c<0 or r+1 > len(image) or c+1 > len(image[0])) or image[r][c] != color1:   
                return
            image[r][c] = color
            fill(r-1,c)
            fill(r+1,c)
            fill(r,c+1)
            fill(r,c-1)
            
            
        fill(sr,sc)
        return image