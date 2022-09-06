class Solution:
    def addDigits(self, num: int) -> int:
        
        s = 0
        while len(str(num)) > 1:
            s+= num//10**(len(str(num))-1)
            num = num % 10**(len(str(num))-1)
        s+=num
        print(f"S= {s}")
        while s > 9:
            s = self.addDigits(s)
        return s