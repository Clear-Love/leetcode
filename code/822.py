'''
Author: lmio 2091319361@qq.com
Date: 2023-08-02 12:45:54
LastEditors: lmio 2091319361@qq.com
Description: 822. 翻转卡片游戏
'''

from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        f = set()
        for i, v in enumerate(fronts):
            if v == backs[i]:
                f.add(v)
        for v in sorted(fronts+backs):
            if v not in f:
                return v
        return 0