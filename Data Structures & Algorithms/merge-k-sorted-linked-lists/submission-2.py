# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        for i in range(1, len(lists)):
            out = self.mergeList(lists[i - 1], lists[i])
            lists[i] = out
        
        return None if not lists else lists[-1]

    
    def mergeList(self, a, b):
        dummy = ListNode()

        node = dummy

        while a and b:
            if a.val < b.val:
                node.next = a
                a = a.next
            else:
                node.next = b
                b = b.next
            node = node.next

        if a:
            node.next = a
        if b:
            node.next = b
        
        return dummy.next