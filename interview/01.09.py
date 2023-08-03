'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 09:39:14
LastEditors: lmio 2091319361@qq.com
Description: 面试题 01.09. 字符串轮转
'''
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == '' and s2 == '':
            return True
        if len(s1) != len(s2):
            return False
        def isRound(i: int) -> bool:
            for j in range(len(s2)):
                if s1[i] != s2[j]:
                    return False
                i = (i+1) % n
            return True
        for i in range(n):
            if isRound(i):
                return True
        return False