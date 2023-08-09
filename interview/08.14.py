'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 20:51:11
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.14. 布尔运算
'''

from functools import cache


class Solution:
    @cache #记忆化搜索
    def countEval(self, s: str, result: int) -> int:
        if len(s) == 1:
            if int(s) == result:
                return 1
            return 0
        cnt = 0
        n = len(s)
        for i in range(1, n, 2):
            if result:
                if s[i] == '&':
                    cnt += self.countEval(s[:i], 1)*self.countEval(s[i+1:], 1)
                elif s[i] == '|':
                    l1 = self.countEval(s[:i], 1)
                    l0 = self.countEval(s[:i], 0)
                    r1 = self.countEval(s[i+1:], 1)
                    r0 = self.countEval(s[i+1:], 0)
                    cnt += l1*(r0+r1)+l0*r1
                else:
                    l1 = self.countEval(s[:i], 1)
                    l0 = self.countEval(s[:i], 0)
                    r1 = self.countEval(s[i+1:], 1)
                    r0 = self.countEval(s[i+1:], 0)
                    cnt += l1*r0
                    cnt += l0*r1
            else:
                if s[i] == '&':
                    l1 = self.countEval(s[:i], 1)
                    l0 = self.countEval(s[:i], 0)
                    r1 = self.countEval(s[i+1:], 1)
                    r0 = self.countEval(s[i+1:], 0)
                    cnt += l0*(r0+r1) + r0*l1
                elif s[i] == '|':
                    cnt += self.countEval(s[:i], 0)*self.countEval(s[i+1:], 0)
                else:
                    l1 = self.countEval(s[:i], 1)
                    l0 = self.countEval(s[:i], 0)
                    r1 = self.countEval(s[i+1:], 1)
                    r0 = self.countEval(s[i+1:], 0)
                    cnt += l1*r1
                    cnt += l0*r0
        return cnt