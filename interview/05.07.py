'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 22:07:37
LastEditors: lmio 2091319361@qq.com
Description: 面试题 05.07. 配对交换
'''

class Solution:
    def exchangeBits(self, num: int) -> int:
        even = 1431655765
        odd = even << 1
        odd = (num&odd) >> 1
        even = (num&even) << 1
        return odd | even