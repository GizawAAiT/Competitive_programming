class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):        
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):  
                # print("index:",(i,j),"val:",(self.matrix[i][j]))
                if i==0 and j!=0:
                    self.matrix[i][j] += self.matrix[i][j-1]
                elif j==0 and i!=0:
                    self.matrix[i][j] += self.matrix[i-1][j]
                elif i!=0:
                    self.matrix[i][j] += (self.matrix[i][j-1] +self.matrix[i-1][j]-self.matrix[i-1][j-1])
        # print(len(self.matrix),self.matrix)
   
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        
        above = self.matrix[r1-1][c2] if r1>0 else 0
        left = self.matrix[r2][c1-1] if c1>0 else 0
        intersection= self.matrix[r1-1][c1-1] if r1>0 and c1>0 else 0
        total = self.matrix[r2][c2]
        # print("T=",total,"L:",left,"Ab:",above,"Inter",intersection)
        return (total + intersection - above-left)
    
    



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)