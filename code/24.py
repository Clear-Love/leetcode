'''
Author: lmio 2091319361@qq.com
Date: 2023-08-06 20:19:33
LastEditors: lmio 2091319361@qq.com
Description: 24. 两两交换链表中的节点
'''

from typing import Optional

from utils.node import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fist = dummy
        if not head:
            return None
        pre, cur = head, head.next
        while cur:
            pre.next = cur.next
            cur.next = pre
            fist.next = cur
            fist = pre
            pre = pre.next
            if not pre:
                break
            cur = pre.next
        return dummy.next