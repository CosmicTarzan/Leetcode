# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        arr = []
        l3 = head

        while list1 is not None or list2 is not None:
            if list1 is not None:
                arr.append(list1.val)
                list1 = list1.next
            if list2 is not None:
                arr.append(list2.val)
                list2 = list2.next

        arr.sort()
        
        for i in arr:
            l3.next = ListNode(i)
            l3 = l3.next

        return head.next