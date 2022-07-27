# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []

        while head.next:
            stack.append(head)
            head = head.next
        print (head)

        while stack:
            cur = stack.pop()
            #print ("cur ="+str(cur))
            print ("cur next="+str(cur.next))
            #print ("cur next next="+str(cur.next.next))
            cur.next.next = cur
            #print (cur.next.next.val)
            #print ("cur next="+str(cur.next))
            cur.next = None
            
            

        return head