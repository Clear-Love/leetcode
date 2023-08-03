'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 19:17:07
LastEditors: lmio 2091319361@qq.com
Description: 面试题 02.02. 返回倒数第 k 个节点
'''

from utils.node import ListNode


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        i = 0
        left, right = head, head
        while i < k:
            right = right.next
            i += 1
        while right:
            right = right.next
            left = left.next
        return left.val
