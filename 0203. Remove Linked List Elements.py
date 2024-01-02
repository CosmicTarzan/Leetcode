class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head2 = ListNode()
        l = head2
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                l.next = ListNode(head.val)
                l = l.next
                head = head.next
        return head2.next
