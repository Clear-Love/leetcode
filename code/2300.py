'''
Author: lmio 2091319361@qq.com
Date: 2023-07-30 20:31:28
LastEditors: lmio 2091319361@qq.com
Description: 2300. 咒语和药水的成功对数
'''

import bisect
import math
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        res = []
        for v in spells:
            target = math.ceil(success/v) 
            i = bisect.bisect_left(potions, target)
            res.append(m - i)
        return res