# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_sum = [float('-inf')]


        def dfs(node):
            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            path_sum = node.val + max(left_max, right_max)
            global_sum[0] = max(global_sum[0], node.val + left_max + right_max)

            return max(0, path_sum)
        
        dfs(root)

        return global_sum[0]