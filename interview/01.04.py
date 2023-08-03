'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 09:01:35
LastEditors: lmio 2091319361@qq.com
Description: 面试题 01.04. 回文排列
'''
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnts = Counter(s)
        can = True
        for v in cnts.values():
            if v & 1 == 1:
                can = not can
                if can:
                    return False
        return True