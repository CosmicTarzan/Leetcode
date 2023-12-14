# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = ListNode(0)
        l = h
        h2 = ListNode(0)
        l2 = h2
        count = 0
        count2 = 0

        while head is not None:
            l.next = ListNode(head.val)
            l = l.next
            head = head.next
            count += 1
        
        h = h.next

        while h is not None:
            if count2 == count - n:
                h = h.next
            else:
                l2.next = ListNode(h.val)
                l2 = l2.next
                h = h.next
            count2 += 1

        return h2.next