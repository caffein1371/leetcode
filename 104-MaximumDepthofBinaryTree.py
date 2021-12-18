#Definition for a binary tree node.
#seen 全体を false に初期化して、todo を空にする
#seen[s] = true として、todo に s を追加する
#todo が空になるまで以下を繰り返す:
#todo から一つ頂点を取り出して v とする
#T(v) の各要素 w に対して、
#seen[w] = true であったならば、何もしない
#そうでなかったら、seen[w] = true として、todo に w を追加する
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        deep = 0
        stack = [(root,1)]
        while stack:
            root,length = stack.pop()
            if not root:
                return 0
            if deep<length:
                deep=length
            if root.left:
                stack.append((root.left,length+1))
            if root.right:
                stack.append((root.right,length+1))
                
        return deep