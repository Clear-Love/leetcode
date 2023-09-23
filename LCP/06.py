'''
Author: lmio 2091319361@qq.com
Date: 2023-09-20 14:13:17
LastEditors: lmio 2091319361@qq.com
Description: LCP 06. 拿硬币
'''

import math
from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum([math.ceil(v/2) for v in coins])