# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA:
            return None
        elif  not headB:
            return None
        
        LNA = headA
        LNB = headB
        while LNA != LNB:
            LNA = headB if not LNA else LNA.next
            LNB = headA if not LNB else LNB.next
        return LNA