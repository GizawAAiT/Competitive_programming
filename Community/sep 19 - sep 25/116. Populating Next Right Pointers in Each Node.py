"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        
        Q = [root]
        while Q:
            l = len(Q)
            nodes = []
            for i in range(l):
                nd = Q.pop(0)
                nodes.append(nd)
                if nd.left:
                    Q.append(nd.left)
                    Q.append(nd.right)
            i = 0
            while i+1 < len(nodes):
                nodes[i].next = nodes[i+1]
                i+=1
            nodes[-1].next = None
        return root
                    
        
        