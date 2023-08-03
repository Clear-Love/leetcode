'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 19:23:25
LastEditors: lmio 2091319361@qq.com
Description: 面试题 02.03. 删除中间节点
'''

from utils.node import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next