class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for w in words:
            if len(w)>=len(pref) and pref == w[:len(pref)]: res +=1
        return res