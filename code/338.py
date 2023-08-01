'''
Author: lmio 2091319361@qq.com
Date: 2023-07-31 16:18:19
LastEditors: lmio 2091319361@qq.com
Description: 338. 比特位计数
'''

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(1, n+1):
            res[i] = res[i&(i-1)]+1
        return res