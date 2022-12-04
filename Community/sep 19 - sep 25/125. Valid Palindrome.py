class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()        
        l = [i for i in s if i.isalnum()]
        i= (len(l)-1)//2
        j = i if len(l)%2 else i+1
        while i>=0:
            if l[i]!=l[j]: 
                return False
            i,j=i-1,j+1
        return True
