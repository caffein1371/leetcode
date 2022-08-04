# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        def help(root):
            if root:
                if  low <=root.val and root.val<=high:
                    self.ans+=root.val
                if low<root.val:
                    help(root.left)
                if root.val<high:
                    help(root.right)
            #print ("ans="+ str(self.ans))
            return self.ans
        return help(root)