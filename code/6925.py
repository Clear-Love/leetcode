'''
Author: lmio 2091319361@qq.com
Date: 2023-08-06 10:30:53
LastEditors: lmio 2091319361@qq.com
Description: 6925. 故障键盘
'''

class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] == 'i':
                res.reverse()
            else:
                res.append(s[i])
        return ''.join(res)