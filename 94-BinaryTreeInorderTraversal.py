# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#wikiより
#間順・中間順・通りがけ順 (英: in-order)
#もしあれば、左の部分木を間順走査する。
#根ノードを調査する。
#もしあれば、右の部分木を間順走査する。
#多分木では定義されない。2分探索木では、間順走査によって走査する順がソートされた順序になるため、よく使われる。
class Solution: 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def help(root,ans):
            if root is not None:
                help(root.left,ans)
                ans.append(root.val)
                help(root.right,ans)
                return ans
            else:
                return 
        return help(root,ans)
        