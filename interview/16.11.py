'''
Author: lmio 2091319361@qq.com
Date: 2023-08-14 18:09:31
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.11. 跳水板
'''

from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter*k]
        res = []
        for i in range(k+1):
            res.append(longer*i + shorter*(k-i))
        return res