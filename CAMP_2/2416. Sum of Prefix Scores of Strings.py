class TrieNode():
    def __init__(self):
        self.children = [None] *27
        self.isLast = False
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Define the trie root
        root = TrieNode()

        # Add each word to the trie:
        for word in words:
            cur = root
            for ch in word:
                order = ord(ch)-96
                if not cur.children[order]:
                    cur.children[order] = TrieNode()
                cur = cur.children[order]
                cur.count += 1
        
        # Calculate the sum for each words and store on res:
        res = []
        for word in words:
            cur = root
            total = 0
            for ch in word:
                cur = cur.children[ord(ch) - 96]
                total += cur.count
            res.append(total)
        
        return res





