# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def help(t1,t2):
            if t1 is not None and t2 is not None:
                #print (t1)
                #print (t2)
                return t1.val == t2.val and help(t1.left,t2.right) and help(t1.right,t2.left)
            else:
                return t1==t2
        
        return help(root,root)