'''
Author: lmio 2091319361@qq.com
Date: 2023-08-07 12:15:25
LastEditors: lmio 2091319361@qq.com
Description: 344. 反转字符串
'''

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1