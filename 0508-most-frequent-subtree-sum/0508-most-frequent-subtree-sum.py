# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        frequency = defaultdict(int)
        max_freq = 0
        
        def dfs(root):
            nonlocal max_freq
            if not root:
                return 0
            
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            subtree_sum = root.val + left_sum + right_sum
            frequency[subtree_sum] += 1
            max_freq = max(max_freq, frequency[subtree_sum])
            
            return subtree_sum
        
        # excute the function dfs() with the root.
        dfs(root)
        
        answer = []
        for key in frequency: 
            
            if frequency[key] == max_freq:
                answer.append(key)
        return answer