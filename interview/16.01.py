'''
Author: lmio 2091319361@qq.com
Date: 2023-08-10 16:40:39
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.01. 交换数字
'''

from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] ^= numbers[1]
        numbers[1] ^= numbers[0]
        numbers[0] ^= numbers[1]
        return numbers