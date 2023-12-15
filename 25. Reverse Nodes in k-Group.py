# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 0
        h = ListNode(0)
        ans = h
        mem = []
        while head is not None:
            counter += 1
            if counter % k > 0:
                mem.append(head.val)
            else:
                ans.next = ListNode(head.val)
                ans = ans.next
                for i in mem[::-1]:
                    ans.next = ListNode(i)
                    ans = ans.next
                mem = []
            head = head.next

        if len(mem) > 0:
            for i in mem:
                ans.next = ListNode(i)
                ans = ans.next
        
        return h.next