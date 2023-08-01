'''
Author: lmio 2091319361@qq.com
Date: 2023-07-31 15:05:09
LastEditors: lmio 2091319361@qq.com
Description: 143. 重排链表
'''

from collections import deque
from typing import Optional

from utils.node import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        def middleNode(head: ListNode) -> ListNode:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            curr = head
            while curr:
                nextTemp = curr.next
                curr.next = prev
                prev = curr
                curr = nextTemp
            return prev
        def mergeList(l1: ListNode, l2: ListNode):
            while l1 and l2:
                l1_tmp = l1.next
                l2_tmp = l2.next
                l1.next = l2
                l1 = l1_tmp
                l2.next = l1
                l2 = l2_tmp
        mid = middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = reverseList(l2)
        mergeList(l1, l2)