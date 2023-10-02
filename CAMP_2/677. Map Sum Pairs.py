class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isLast = False
        self.val = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for char in key:
            indx = ord(char) - 97 # ord("a") == 97.
            if not cur.children[indx]:
                cur.children[indx] = TrieNode()
            cur = cur.children[indx]
        cur.isLast = True
        cur.val = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            indx = ord(char) - 97 # ord("a") == 97.
            if not cur.children[indx]:
                return 0
            cur = cur.children[indx]
        
        result = 0
        que = [cur]
        while que:
            length = len(que)
            node = que.pop()
            if node.isLast: 
                result += node.val 
            for child in node.children:
                if child:
                    que.append(child) 
        
        return result                 
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)