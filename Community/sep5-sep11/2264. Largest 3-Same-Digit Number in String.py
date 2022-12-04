class Solution:
    def largestGoodInteger(self, num: str) -> str:
        longest = -1
        
        a=0
        b=0
        while b<len(num):
            if num[b]!=num[a] and (b-a) >= 3:
                longest = max(longest,int(num[a])) 
                a = b 
            elif num[b]!=num[a] :
                a = b
            b+=1
            print(a,b,longest)
        if b-a >=3:
            longest = max(longest,int(num[a])) 
        if longest == -1:
            return ""
        return str(longest)*3