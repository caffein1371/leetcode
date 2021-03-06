# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                if low<= node.val and node.val<=high:
                    self.ans+=node.val
                if node.val>low:
                    dfs(node.left)
                if high>node.val:
                    dfs(node.right)
                    
        self.ans=0
        dfs(root)
        return self.ans
            