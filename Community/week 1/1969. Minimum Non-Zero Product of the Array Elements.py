class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        if p ==1:
            return p     
        x=2**p
        Mod=10**9 + 7
        return (pow(x -2, x/2 - 1, Mod) * (x - 1)) % (Mod)