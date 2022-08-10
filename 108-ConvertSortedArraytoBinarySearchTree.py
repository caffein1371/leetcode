# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        ans = TreeNode()
        def help(a,ans: TreeNode) ->TreeNode:
            if not ans:
                #ans.val = a
                print (ans.type())
                return ans
            if ans.val>=a:
                help(a,ans.right)
            else:
                help(a,ans.left)
            return ans    
            
        #print (ans.val)
        for i in nums:
            print (i)
            ans = help(i,ans)

        return ans