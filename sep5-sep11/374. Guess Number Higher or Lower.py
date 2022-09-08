# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        a, b = -1, n
        while a<b-1:
            m = (a+b)//2
            if guess(m) == 0:
                print(f"mid : {m}")
                return m
            if guess(m) == 1:
                a = m
            else:
                b = m
        return a+1


        

        