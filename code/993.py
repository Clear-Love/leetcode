'''
Author: lmio 2091319361@qq.com
Date: 2024-03-18 22:42:00
LastEditors: lmio 2091319361@qq.com
Description: 993. 二叉树的堂兄弟节点
'''

from typing import Optional

from utils.node import TreeNode


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        while q:
            tmp = []
            m = set()
            while q:
                node = q.pop()
                arr = []
                if node.left:
                    v = node.left.val
                    if v == x and y in m:
                        return True
                    if v == y and x in m:
                        return True
                    arr.append(v)
                    tmp.append(node.left)
                if node.right:
                    v = node.right.val
                    print(v, m)
                    if v == x and y in m:
                        return True
                    if v == y and x in m:
                        return True
                    arr.append(v)
                    tmp.append(node.right)
                for a in arr:
                    m.add(a)
            q = tmp
        return False
