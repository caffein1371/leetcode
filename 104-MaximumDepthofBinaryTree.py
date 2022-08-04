# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def help(root):
            d1 = 0
            d2 = 0
            if root is not None:
                d1 = help(root.left)
                d2 = help(root.right)
                
                return 1+max(d1,d2)
            else:
                return 0
                
            
        return help(root)