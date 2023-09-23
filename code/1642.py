'''
Author: lmio 2091319361@qq.com
Date: 2023-09-22 21:55:41
LastEditors: lmio 2091319361@qq.com
Description: 1642. 可以到达的最远建筑
'''

import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        q = [] 
        brick_remain = bricks

        for i in range(1, n):
            if heights[i] < heights[i-1]:
                continue
            # 高度差
            d = heights[i] - heights[i-1]
            if len(q) < ladders:
                heapq.heappush(q, d)
            elif q and d > q[0]:
                brick_remain -= heapq.heappop(q) # 原来的那架梯子改为消耗砖头
                if brick_remain < 0:
                    return i-1 # 砖头不足以完成
                heapq.heappush(q, d) # 当前位置使用梯子
            else: # 使用砖头
                brick_remain -= d 
                if brick_remain < 0:
                    return i-1 # 砖头不足以完成
        return n-1