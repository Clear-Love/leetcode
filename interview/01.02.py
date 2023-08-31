'''
Author: lmio 2091319361@qq.com
Date: 2023-08-31 19:30:45
LastEditors: lmio 2091319361@qq.com
Description: 面试题 01.02. 判定是否互为字符重排
'''

from collections import Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        s1 = Counter(s1)
        s2 = Counter(s2)
        return s1 == s2