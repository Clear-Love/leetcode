'''
Author: lmio 2091319361@qq.com
Date: 2023-09-02 13:54:34
LastEditors: lmio 2091319361@qq.com
Description: 2511. 最多可以摧毁的敌人城堡数目
'''

from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last = -1
        res = 0
        for i, v in enumerate(forts):
            if v == 0:
                continue
            if last != -1 and v != forts[last]:
                res = max(res, i-last-1)
            last = i
        return res