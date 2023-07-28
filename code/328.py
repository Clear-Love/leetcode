'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 21:20:58
LastEditors: lmio 2091319361@qq.com
Description: 328. 奇偶链表
'''
from typing import Optional

from utils.node import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        isOdd = True
        odd = ListNode()
        even = ListNode()
        node = head
        op = odd
        ep = even
        while node:
            if isOdd:
                op.next = ListNode(node.val)
                op = op.next
            else:
                ep.next = ListNode(node.val)
                ep = ep.next
            isOdd = not isOdd
            node = node.next
        op.next = even.next
        return odd.next