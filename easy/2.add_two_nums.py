# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        p1 = l1
        p2 = l2
        jinwei = 0
        while p1 != None or p2 != None:
            s = jinwei
            if p1 != None:
                s += p1.val
                p1 = p1.next
            if p2 != None:
                s += p2.val
                p2 = p2.next
            n = int(s%10)
            curr.next = ListNode(n)
            curr = curr.next
            if s >= 10:
                jinwei = 1
            else:
                jinwei = 0
        if jinwei == 1:
            curr.next = ListNode(1)
        return head.next