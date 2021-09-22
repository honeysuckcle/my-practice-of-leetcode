"""
Date: 2021/9/22
链表
执行用时：28 ms, 在所有 Python3 提交中击败了98.91%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了29.82%的用户
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import List

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        curr, count = head, 0
        while curr != None:
            count += 1
            curr = curr.next
        
        q, r = int(count / k), int(count % k)
        curr = head
        res = []

        for i in range(k):
            sub_len = q
            if i < r:
                sub_len += 1
            res.append(curr)
            for j in range(sub_len - 1):
                if curr != None:
                    curr = curr.next
                else:
                    break
            if curr != None:
                next_node = curr.next
                curr.next = None
                curr = next_node
        return res
            
            

