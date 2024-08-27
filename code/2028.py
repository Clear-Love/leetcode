'''
Author: lmio 2091319361@qq.com
Date: 2024-05-27 15:20:38
LastEditors: lmio 2091319361@qq.com
Description: 2028. 找出缺失的观测数据
'''

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = (n+m)*mean - sum(rolls)
        avg = s // n
        if avg < 1 or avg > 6:
            return []
        r = s % n
        res = [avg]*n
        i = 0
        while r:
            res[i] += 1
            if res[i] > 6:
                return []
            r -= 1
            if r == 0:
                break
            i = (i+1)%n
        return res