class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        f = Counter(words)
        
        a = sorted(f, key = lambda x: (-f[x],x)) 
        return a[:k]