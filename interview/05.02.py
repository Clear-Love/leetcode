'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 20:03:41
LastEditors: lmio 2091319361@qq.com
Description: 面试题 05.02. 二进制数转字符串
'''

class Solution:
    def printBin(self, num: float) -> str:
        res = ''
        mod = 0.5
        for _ in range(32):
            print(num)
            if num == 0:
                return res
            if num//mod:
                res += '1'
            else:
                res += '0'
            num = num % mod
            mod /= 2
        return 'ERROR'