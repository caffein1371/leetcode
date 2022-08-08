# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def help(root,ans):
            if root:
                help(root.left,ans)
                help(root.right,ans)
                #print (root.val)
                ans.append(root.val)
                return ans
            else:
                return
        return help(root,ans)
                