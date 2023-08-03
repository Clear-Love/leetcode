'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 19:37:31
LastEditors: lmio 2091319361@qq.com
Description: 面试题 02.04. 分割链表
'''

from utils.node import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre = ListNode()
        next = ListNode()
        node = head
        n, m = pre, next
        while node:
            tmp = node.next
            node.next = None
            if node.val < x:
                pre.next = node
                pre = pre.next
            else:
                next.next = node
                next = next.next
            node = tmp
        pre.next = m.next
        return n.next
            