# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        res_p = res
        carryover = 0
        
        while l1 or l2 or carryover:
            if l1:
                carryover += l1.val
                l1 = l1.next
            if l2:
                carryover += l2.val
                l2 = l2.next

            res_p.next = ListNode(carryover % 10)
            res_p = res_p.next
            carryover = carryover // 10

        return res.next
