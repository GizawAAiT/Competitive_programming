class TrieNode:
    def __init__(self):
        self.children = [None]*28
        # self.isLast = False
        self.indx = -1

class WordFilter:

    def __init__(self, words: List[str]):
        # define the trienode
        self.root = TrieNode()

        # Add the words to the trie node 
        for i, word in enumerate(words):
            for _ in range(len(word)):
                cur = self.root
                suf_pref = word[_:] + '`' + word
                for ch in suf_pref:
                    order = ord(ch)-96
                    if not cur.children[order]: 
                        cur.children[order] = TrieNode()
                    cur = cur.children[order]
                    cur.indx = i
        

    def f(self, pref: str, suff: str) -> int:
        cur = self.root
        for ch in suff + '`' + pref:
            order = ord(ch) -96
            if not cur.children[order]: 
                return -1
            cur = cur.children[order]
        return cur.indx 
        
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
