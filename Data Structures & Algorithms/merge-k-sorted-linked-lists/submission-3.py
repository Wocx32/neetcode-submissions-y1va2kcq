# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i - 1], lists[i])
        
        return lists[-1]
    
    def mergeLists(self, lis1, lis2):

        dummy = ListNode()
        tail = dummy
        
        while lis1 and lis2:
            if lis1.val < lis2.val:
                tail.next = lis1
                lis1 = lis1.next
            else:
                tail.next = lis2
                lis2 = lis2.next
            
            tail = tail.next
        
        if lis1:
            tail.next = lis1
        else:
            tail.next = lis2
        
        return dummy.next