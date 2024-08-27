'''
Author: lmio 2091319361@qq.com
Date: 2024-03-07 17:50:28
LastEditors: lmio 2091319361@qq.com
Description: 2575. 找出字符串的可整除数组
'''

from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        remain = 0
        res = []
        for w in word:
            remain = (remain*10 + int(w))%m
            if remain == 0:
                res.append(1)
            else:
                res.append(0)
        return res