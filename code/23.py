'''
Author: lmio 2091319361@qq.com
Date: 2023-08-12 20:53:28
LastEditors: lmio 2091319361@qq.com
Description: 23. 合并 K 个升序链表
'''

import heapq
from typing import List, Optional

from utils.node import ListNode

ListNode.__lt__ = lambda a, b: a.val < b.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = ListNode()
        dummy = cur
        h = [node for node in lists if node]
        heapq.heapify(h)
        while h:
            node = heapq.heappop(h)
            cur.next = node
            if node.next:
                heapq.heappush(h, node.next)
            cur = cur.next
        return dummy.next