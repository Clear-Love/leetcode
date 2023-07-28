'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 18:01:23
LastEditors: lmio 2091319361@qq.com
Description: 2095. 删除链表的中间节点
'''

from typing import Optional

from utils.node import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        flow, fast = dummy, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            flow = flow.next
        flow.next = flow.next.next
        return dummy.next