# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = ListNode()
        l = head2
        if not head:
            return head2.next
        value = head.val
        head = head.next
        l.next = ListNode(value)
        l = l.next
        while head is not None:
            if head.val == value:
                head = head.next
                continue
            else:
                value = head.val
                head = head.next
                l.next = ListNode(value)
                l = l.next
        return head2.next

                
