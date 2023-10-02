class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isLast = False
        self.val = ""

class Solution:
    def __init__(self):
        self.ans = []
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        root.isLast = True
        for word in words:
            cur = root
            for char in word:
                indx = ord(char) - 97 #
                if not cur.children[indx]:
                    cur.children[indx] = TrieNode()
                    cur.children[indx].val = char
                cur = cur.children[indx]
                
            cur.isLast = True

        def dfs(cur, path):
            if len(self.ans) < len(path):
                self.ans = path[:]
            for child in cur.children:
                if child and child.isLast:
                    path.append(child.val)
                    dfs(child, path)
                    path.pop()

        dfs(root, [])
        return "".join(self.ans)