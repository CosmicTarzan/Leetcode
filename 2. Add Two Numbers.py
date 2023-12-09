class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        l3 = head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            s = digit1 + digit2 + carry
            digit = s % 10
            carry = s // 10

            l3.next = ListNode(digit)
            l3 = l3.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return head.next