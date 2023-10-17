'''
Author: lmio 2091319361@qq.com
Date: 2023-10-17 18:34:27
LastEditors: lmio 2091319361@qq.com
Description: 947. 移除最多的同行或同列石头
'''

from collections import defaultdict
from typing import List

from utils.unionFind import unionFind


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = unionFind()
        for x, y in stones:
            x += 10001
            uf.union(x, y)
        link = set(uf.find(y) for _, y in stones)
        return len(stones) - len(link)