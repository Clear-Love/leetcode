'''
Author: lmio 2091319361@qq.com
Date: 2024-04-07 15:45:29
LastEditors: lmio 2091319361@qq.com
Description: 1600. 王位继承顺序
'''

from collections import defaultdict
from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dead = set()
        self.g = defaultdict(list)

    def birth(self, parentName: str, childName: str) -> None:
        self.g[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(x: str):
            if x not in self.dead:
                ans.append(x)
            for y in self.g[x]:
                dfs(y)

        ans = []
        dfs(self.king)
        return ans