# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxdeep = 0
        stack = [(root,1)]
        ans = 0
        while stack:
            root,length = stack.pop()
            if not root:
                return 0
            if maxdeep<length:
                maxdeep=length
                ans=root.val
            elif maxdeep==length:
                ans+=root.val
            if root.left:
                stack.append((root.left,length+1))
            if root.right:
                stack.append((root.right,length+1))
            
        return ans