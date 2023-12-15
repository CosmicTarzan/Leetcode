# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    counter = 0
    h = ListNode(0)
    ans = h
    mem = None
    while head is not None:
        counter += 1
        if counter % 2 == 1:
            mem = head.val
        else:
            ans.next = ListNode(head.val)
            ans = ans.next
            ans.next = ListNode(mem)
            ans = ans.next
            mem = None

        head = head.next

    if mem != None:
        ans.next = ListNode(mem)
        ans = ans.next
    
    return h.next