# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        arr = []
        l3 = head

        for listK in lists:
            while listK is not None:
                if listK is not None:
                    arr.append(listK.val)
                    listK = listK.next

        arr.sort()
        for i in arr:

            l3.next = ListNode(i)
            l3 = l3.next

        return head.next