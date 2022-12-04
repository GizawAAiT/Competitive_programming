class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 0
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            i = 1
            length = len(digits)
            while  i <= length and digits[-i]==9:
                digits[-i]=0
                i+=1
            if i > length:
                digits.insert(0,1)
            else:
                digits[-i]+=1
        return digits
                
