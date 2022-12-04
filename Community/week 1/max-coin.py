class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        s=0
        piles=sorted(piles)
        for i in range(len(piles)//3):
            s +=piles[-(i+1)*2]
        return s