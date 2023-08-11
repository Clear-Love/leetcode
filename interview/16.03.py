'''
Author: lmio 2091319361@qq.com
Date: 2023-08-10 16:46:52
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.03. 交点
'''

from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        def inLine(x, y) -> bool:
            for s, e in ((start1, end1), (start2, end2)):
                minx = min(s[0], e[0])
                maxx = max(s[0], e[0])
                miny = min(s[1], e[1])
                maxy = max(s[1], e[1])
                if not(minx <= x <= maxx and miny <= y <= maxy):
                    return False
            return True
        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2
        # 向量叉乘
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        # 两条直线内积
        c1 = x1 * y2 - y1 * x2
        c2 = x3 * y4 - y3 * x4
        # 检查直线段是否平行
        if abs(denominator) < 1e-6:
            # 边界特殊判定
            if c1 != c2:
                return []
            point = sorted([start1, end1, start2, end2])[1]
            if inLine(*point):
                return point
            return []
        # 计算交点的坐标
        x = (c1 * (x3 - x4) - (x1 - x2) * c2) / denominator
        y = (c1 * (y3 - y4) - (y1 - y2) * c2) / denominator
        # 检查交点是否在两条线段上
        if inLine(x, y):
            return [x, y]
        else:
            return []