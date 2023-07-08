'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 19:02:30
LastEditors: lmio 2091319361@qq.com
Description: 138. 复制带随机指针的链表
'''

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    nodeMap = {}
    def newNode(node: Node) -> Node:
        if not node:
            return None
        if node in nodeMap:
            return nodeMap[node]
        res = Node(node.val)
        nodeMap[node] = res
        res.next = newNode(node.next)
        res.random = newNode(node.random)
        return res
    return newNode(head)
        