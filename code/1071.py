'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 16:58:49
LastEditors: lmio 2091319361@qq.com
Description: 1071. 字符串的最大公因子
'''
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_len = math.gcd(len(str1), len(str2))
        gcd_str = str1[: gcd_len]
        if str1 + str2 == str2 + str1:
            return gcd_str
        return ''