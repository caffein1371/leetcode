# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        #行きがけ法
        def preorder(root,ans):
            if not root:
                return 0
            #左と右の最大値の深さを求める
            L = preorder(root.left,ans)
            R = preorder(root.right,ans)
            
            return 1+max(L,R)
            
        return preorder(root,ans)
            
            
        