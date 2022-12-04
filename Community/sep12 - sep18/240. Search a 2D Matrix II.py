class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]: 
            return False
        
        def bin(l):
            a, b = -1, len(l)
            while a<b-1:
                m = (a+b)//2
                if target == l[m]:
                    return True
                elif target < l[m]:
                    b = m
                else:
                    a = m
            return False
               
        i = 0
        while i < len(matrix):
            if bin(matrix[i]): 
                return True
            i+=1
        return False
                    
                    
                    