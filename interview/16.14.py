'''
Author: lmio 2091319361@qq.com
Date: 2023-08-14 19:39:32
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.14. 最佳直线
'''

from collections import defaultdict
from typing import List


class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(points)):
            x,y = points[i]
            dict = defaultdict(list)
            for j in range(i+1,len(points)):
                tx,ty = points[j]
                # 斜率不存在
                if tx - x == 0:
                    dict["inf"].append(j)
                else:
                    k = (ty-y)/(tx-x)
                    dict[k].append(j)
            for k, v in dict.items():
                if len(v)+1 > len(res):
                    res = [i] + v
        return res[0:2]