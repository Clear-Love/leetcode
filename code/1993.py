'''
Author: lmio 2091319361@qq.com
Date: 2023-09-23 10:23:07
LastEditors: lmio 2091319361@qq.com
Description: 1993. 树上的操作
'''

from collections import defaultdict
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = defaultdict(list)
        for i, v in enumerate(parent):
            if v != -1:
                self.children[v].append(i)
        self.locked = {}

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False
        self.locked.pop(num)
        return True

    def upgrade(self, num: int, user: int) -> bool:
        p = num
        while p != -1:
            if p in self.locked:
                return False
            p = self.parent[p]
        lock_child = []
        q = self.children[num].copy()
        while q:
            node = q.pop()
            if node in self.locked:
                lock_child.append(node)
            q += self.children[node]
        if not lock_child:
            return False
        for v in lock_child:
            self.locked.pop(v)
        self.locked[num] = user
        return True