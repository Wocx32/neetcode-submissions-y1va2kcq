# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        res = ListNode()
        dummy = res
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s // 10
            val = s % 10

            dummy.next = ListNode(val)

            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        
        if l1 or l2:
            node = l1 if l1 else l2
            while node:
                s = node.val + carry
                carry = s // 10
                val = s % 10

                dummy.next = ListNode(val)
                node = node.next
                dummy = dummy.next
        
        if carry:
            dummy.next = ListNode(carry)

        return res.next