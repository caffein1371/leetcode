# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        pointer = result
        while (l1 or l2 or carry):
            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0
            #繰り上がりの値をたす
            summation = first_num + second_num + carry
            #１０で割ったあまりを求める
            num = summation % 10
            #10で割ったものが次のノードに足されるので10で割る
            carry = summation // 10
            #次のpointerを連結リストで初期化
            pointer.next = ListNode(num)
            #ポインターを次へ移す
            pointer = pointer.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next