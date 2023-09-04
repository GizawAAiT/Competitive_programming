class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        
        
        def inbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))
         
        
        def dfs(image, R, C, color, center_color):
            
            if not inbound(R, C) or image[R][C] != center_color or visited[R][C]:
                
                return
             
            image[R][C] = color 
            visited[R][C] = True
            dfs(image, R-1, C, color, center_color)
            dfs(image, R, C-1, color, center_color)
            dfs(image, R+1, C, color, center_color)
            dfs(image, R, C+1, color, center_color) 
        
        
        center_color = image[sr][sc] 
        
        dfs(image, sr, sc, color, center_color) 
        
        return image
        
            
                
