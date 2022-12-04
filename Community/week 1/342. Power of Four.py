class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        while n>=3:
            n/=4.0
            print n
        if n==1.0 :
            return True
        return False