'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 11:01:18
LastEditors: lmio 2091319361@qq.com
Description: 面试题 02.01. 移除重复节点
'''
from utils.node import ListNode


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        visited = set()
        while cur:
            if cur.val in visited:
                pre.next = cur.next
            else:
                visited.add(cur.val)
                pre = cur
            cur = cur.next
        return head