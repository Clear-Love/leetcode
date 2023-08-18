'''
Author: lmio 2091319361@qq.com
Date: 2023-08-13 10:56:31
LastEditors: lmio 2091319361@qq.com
Description: 6914. 翻倍以链表形式表示的数字
'''

from typing import Optional

from utils.node import ListNode


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            carry, n = divmod(cur.val >> 1, 10)
            pre.val += carry
            cur.val = n
            pre = cur
            cur = cur.next
        if dummy.val != 0:
            return dummy
        return dummy.next