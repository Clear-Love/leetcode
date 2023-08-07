'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 13:28:35
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.03. 特定深度节点链表
'''

from collections import deque
from typing import List
from utils.node import ListNode, TreeNode


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        queue = deque()
        queue.append(tree)
        res = []
        while queue:
            node = ListNode()
            tmp = deque()
            head = node
            while queue:
                cur = queue.popleft()
                node.next = ListNode(cur.val)
                node = node.next
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            res.append(head.next)
            queue = tmp
        return res