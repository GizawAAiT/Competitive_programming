class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        left = top = 0
        right = len(mat[0])
        bottom = len(mat)
        
        flattened = []
        while left<right and top<bottom:
            #top
            for j in range(left, right):
                flattened.append(mat[top][j])
            #right
            for i in range(top+1, bottom):
                flattened.append(mat[i][right-1])
            #bottom
            for j in range(right-2, left-1,-1):
                
                if top<bottom-1:
                    flattened.append(mat[bottom-1][j])
            #left
            for i in range(bottom-2, top,-1):
                if left<right-1:
                    flattened.append(mat[i][left])
            top +=1
            left +=1
            right -=1
            bottom -=1
            
        return flattened