'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 20:52:13
LastEditors: lmio 2091319361@qq.com
Description: 面试题 02.06. 回文链表
'''

from utils.node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals == vals[::-1]