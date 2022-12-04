class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        
        b = len(x)//2
        
        if len(x)%2:
            a= b
        else :
            a = b-1
            
        while a>-1:
            if x[a]!=x[b]:
                return False
            a-=1
            b+=1
        return True