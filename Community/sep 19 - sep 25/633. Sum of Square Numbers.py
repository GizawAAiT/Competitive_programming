class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<3:return True
        
             # ...brute force
        # sq=[i**2 for i in range(int(sqrt(c))+2)]
        # print(sq)
        # for i in range(len(sq)):
        #     a,b=i-1,len(sq)
        #     target=c-sq[i]
        #     while a<b-1:
        #         m=(a+b)//2
        #         if sq[m]==target:return True
        #         if sq[m]<target: a=m
        #         else: b=m
        # return False
#         """use math sqrt help.."""
        arr=[sqrt(c-i**2) for i in range(int(sqrt(c))+1)] 
        for i in range(len(arr)): 
            if int(arr[i])==arr[i]:return True
        return False