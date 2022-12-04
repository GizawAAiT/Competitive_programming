class Solution:
    def intToRoman(self, n: int) -> str:
        s = ""
        if n>=1000:
            s = s + str("M"* (n//1000)) 
            n = n % 1000
        rom = [("C","D","M"),("X","L","C"),("I","V","X")]
        
        for i in range(3):
            m = n//10**(2-i)
            n = n % 10**(2-i)
            if m == 4:
                s = s + rom[i][0] + rom[i][1]
            elif m == 9:
                s = s + rom[i][0] + rom[i][2]
            else:
                five = int(m>=5)
                if five:
                    unit = m-5
                else:
                    unit = m
                s = s + rom[i][1]*five + rom[i][0]*unit
        return s
        

        