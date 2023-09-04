# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequency = defaultdict(int)
        max_freq = 0
        def dfs(root):
            nonlocal max_freq
            if not root:
                return
            frequency[root.val] += 1
            max_freq = max(max_freq, frequency[root.val] ) 
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        
        ans = []
        for key, value in frequency.items():
            if value == max_freq:
                ans.append(key)
        return ans