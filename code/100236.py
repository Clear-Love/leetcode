'''
Author: lmio 2091319361@qq.com
Date: 2024-03-17 10:41:45
LastEditors: lmio 2091319361@qq.com
Description: 100236. 统计以给定字符开头和结尾的子字符串总数
'''

import math


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = 0
        for w in s:
            if w == c:
                cnt += 1
        return cnt + math.comb(cnt, 2)