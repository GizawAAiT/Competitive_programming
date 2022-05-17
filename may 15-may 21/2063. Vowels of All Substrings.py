class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        length = len(word)
        sum = 0
        for v,x in enumerate(word):
            if x in ('aeuio'):
                sum += (v+1)*(length-v)
        return sum