from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        res = iter = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                iter.next = list1
                list1 = list1.next
            else:
                iter.next = list2
                list2 = list2.next

            iter = iter.next

        if list1:
            iter.next = list1
        elif list2:
            iter.next = list2

        return res.next

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            lists[0] = self.mergeTwoLists(lists[0], lists[1])
            lists.pop(1)

        return lists[0]
