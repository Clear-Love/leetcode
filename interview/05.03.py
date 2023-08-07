'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 20:09:41
LastEditors: lmio 2091319361@qq.com
Description: 面试题 05.03. 翻转数位
'''

class Solution:
    def reverseBits(self, num: int) -> int:
        length = 0
        cur = 0
        res = 1
        for _ in range(32):
            if num & 1:
                cur += 1
                length += 1
            else:
                length = cur + 1
                cur = 0
            res = max(res, length)
            num = num >> 1
        return res