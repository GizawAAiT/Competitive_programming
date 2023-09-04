class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print(s)
        num = "0"
        if len(s) ==0:
            return "0"
        sign = "+"
        i = 0
        if (not s[i].isdigit() ) and not(s[i] in ["-","+"]):
            x = ["+","-"]
            # print(f"isdigit : {not s[i].isdigit() and  not(s[i] in x)}") 
            return int(num)
        if s[i] in ["-","+"]:
            sign = s[i]
            i +=1
        if sign == "-":
            num = "-"+ num
        
        
        while i< len(s) and s[i].isdigit() :
            num = num + s[i]
            i+=1
        num = int(num)
        if num < -2**31:
            num = -2**31
        if num > 2**31-1:
            num = 2**31-1
        return int(num)
       