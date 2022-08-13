# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.depth = 0
        self.dict = {}
        
        def help(root):
            if not root:
                return 0
            L = help(root.left)
            R = help(root.right)

            if self.depth>=L+R:
                self.depth = L+R
                #print (L+R)
                self.ans+=root.val
                self.dict[self.depth]=self.ans
                #print (root.val)

            return 1+max(L,R)
        
        help(root)
        print (self.dict)
        return max(self.dict.values())