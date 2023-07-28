'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 14:21:29
LastEditors: lmio 2091319361@qq.com
Description: 2390. 从字符串中移除星号
'''

class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for ch in s:
            if ch == '*':
                res.pop()
                continue
            res.append(ch)
        return ''.join(res)