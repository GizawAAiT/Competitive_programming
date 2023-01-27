class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<3:return True
        
        arr=[sqrt(c-i**2) for i in range(int(sqrt(c))+1)] 
        for i in range(len(arr)): 
            if int(arr[i])==arr[i]:return True
        return False