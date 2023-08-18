'''
Author: lmio 2091319361@qq.com
Date: 2023-08-16 21:08:32
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.18. 模式匹配
'''

from collections import Counter


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        cnts  = Counter(pattern)
        aCnt, bCnt = cnts['a'], cnts['b']
        lv = len(value)
        def valid(i: int, j: int) ->bool:
            k = 0
            ia = pattern.find('a')
            ib = pattern.find('b')
            a = value[ia*j:ia*j+i] if ia != -1 else '*'
            b = value[ib*i:ib*i+j] if ib != -1 else '*'
            if a == b:
                return False
            for ch in pattern:
                if ch == 'a':
                    if not value.startswith(a, k):
                        return False
                    k += i
                else:
                    if not value.startswith(b, k):
                        return False
                    k += j
            return k == lv
        if aCnt == 0 and bCnt == 0:
            return not value
        elif aCnt == 0:
            return valid(0, lv//bCnt)
        elif bCnt == 0:
            return valid(lv//aCnt, 0)
        # 遍历a字符串长度
        for i in range(0, lv//aCnt+1):
            j = (lv-(aCnt*i))//bCnt
            if i*aCnt + j*bCnt != lv:
                continue
            if valid(i, j):
                return True
        return False