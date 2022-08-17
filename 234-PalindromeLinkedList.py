# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        anslist = []
        def stack(head):
            if head:
                anslist.append(head.val)
                stack(head.next)
            else:
                return 
        stack(head)
        return anslist==anslist[::-1]