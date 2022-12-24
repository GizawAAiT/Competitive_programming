class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            d[order[i]]= i
        
        def check_order(w1, w2, m, n):
            i = 0 
            while i < m and i < n:
                if d[w1[i]] == d[w2[i]]: i+=1
                else: return d[w1[i]] < d[w2[i]]
            return m<=n

        for i in range(len(words)-1):
            if not check_order(words[i], words[i+1], len(words[i]), len(words[i+1])): return False
        return True

