'''
Author: lmio 2091319361@qq.com
Date: 2023-09-26 13:52:01
LastEditors: lmio 2091319361@qq.com
Description: 2582. 递枕头
'''

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x, y = divmod(time, n-1)
        # 奇数
        if x&1:
            return n-y
        return y+1