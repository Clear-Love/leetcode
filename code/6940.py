'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 22:38:38
LastEditors: lmio 2091319361@qq.com
Description: 6940. 在链表中插入最大公约数
'''

import math
from typing import Optional

from utils.node import ListNode


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = head, head.next
        if not cur:
            return head
        while cur:
            val = math.gcd(pre.val, cur.val)
            pre.next = ListNode(val, next=cur)
            pre = cur
            cur = cur.next
        return head