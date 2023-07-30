'''
Author: lmio 2091319361@qq.com
Date: 2023-07-30 14:52:46
LastEditors: lmio 2091319361@qq.com
Description: 142. 环形链表 II
'''
from typing import Optional

from utils.node import ListNode


class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not fast or not fast.next: 
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow: 
                break
        slow = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast