'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 22:51:13
LastEditors: lmio 2091319361@qq.com
Description: 面试题 02.08. 环路检测
'''

from utils.node import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow