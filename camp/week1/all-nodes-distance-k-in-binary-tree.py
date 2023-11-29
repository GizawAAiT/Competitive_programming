# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def populateGraphDfs(root):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                populateGraphDfs(root.left)
            
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                populateGraphDfs(root.right)

        populateGraphDfs(root)

        visited = set([target.val])
        deq = deque([target.val])
        for _ in range(k):
            if len(deq) == 0: return []
            size = len(deq)
            for _ in range(size):
                node = deq.popleft()
                for child in graph[node]:
                    if child not in visited:
                        deq.append(child)
                        visited.add(child)
                        
        return list(deq)






