'''
Author: lmio 2091319361@qq.com
Date: 2024-03-13 17:34:14
LastEditors: lmio 2091319361@qq.com
Description: 2864. 最大二进制奇数
'''

from typing import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        cnts = Counter(s)
        return ''.join(['1']*(cnts['1']-1) + ['0']*cnts['0'] + ['1'])