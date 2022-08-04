# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        depth = 0
        def help(root,depth):
            d1 = 0
            d2 = 0
            if root is not None:
                d1 = help(root.left,depth)
                d2 = help(root.right,depth)
                
                return 1+max(d1,d2)
            return depth
                
            
        return help(root,depth)