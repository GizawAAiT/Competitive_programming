class Solution:
    def findComplement(self, num: int) -> int:
        exp = math.floor(math.log2(num) )  + 1 
        # print(exp)
        return num^(2**exp-1)