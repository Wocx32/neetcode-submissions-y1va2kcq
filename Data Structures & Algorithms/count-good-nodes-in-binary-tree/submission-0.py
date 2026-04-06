# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, maxSoFar):
            if not root:
                return 0

            goodNode = 0

            if root.val >= maxSoFar:
                goodNode = 1
            
            left = dfs(root.left, max(maxSoFar, root.val))
            right = dfs(root.right, max(maxSoFar, root.val))
        
            return left + right + goodNode

        return dfs(root, root.val)
