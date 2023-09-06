'''
Author: lmio 2091319361@qq.com
Date: 2023-09-01 15:11:38
LastEditors: lmio 2091319361@qq.com
Description: 1556. 千位分隔数
'''

class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []
        s = str(n)
        size = len(s)
        for i in range(size):
            if i and (size-i)%3 == 0:
                res.extend(['.', s[i]])
            else:
                res.append(s[i])
        return ''.join(res)