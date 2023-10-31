'''
Author: lmio 2091319361@qq.com
Date: 2023-10-26 00:04:57
LastEditors: lmio 2091319361@qq.com
Description: 2520. 统计能整除数字的位数
'''

class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for val in str(num):
            if num%int(val) == 0:
                res += 1
        return res