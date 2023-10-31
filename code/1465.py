'''
Author: lmio 2091319361@qq.com
Date: 2023-10-27 13:26:57
LastEditors: lmio 2091319361@qq.com
Description: 1465. 切割后面积最大的蛋糕
'''

from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9+7
        horizontalCuts.sort()
        verticalCuts.sort()
        mh, mw = max(h-horizontalCuts[-1], horizontalCuts[0]), max(w-verticalCuts[-1], verticalCuts[0])
        for i in range(1, len(horizontalCuts)):
            mh = max(mh, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            mw = max(mw, verticalCuts[i]-verticalCuts[i-1])
        return (mh*mw)%MOD