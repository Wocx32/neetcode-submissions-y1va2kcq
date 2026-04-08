# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def validate(node, l_range, r_range):
            if not node:
                return True
            
            if node.val < r_range and node.val > l_range:
                return (validate(node.left, l_range, node.val)
                    and validate(node.right, node.val, r_range)
                )
            else:
                return False
        
        return validate(root, float('-inf'), float('inf'))