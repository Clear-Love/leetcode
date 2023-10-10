'''
Author: lmio 2091319361@qq.com
Date: 2023-10-08 21:15:49
LastEditors: lmio 2091319361@qq.com
Description: 100103. 分类求和并作差
'''

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(1, n+1):
            if i%m:
                res += i
            else:
                res -= i
        return res