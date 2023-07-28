'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 14:27:56
LastEditors: lmio 2091319361@qq.com
Description: 735. 行星碰撞
'''

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for v in asteroids:
            while res and res[-1] > 0 and v < 0:
                t = res.pop()
                if t == -v:
                    v = 0
                    break
                v = t if t > -v else v
            if v: res.append(v)
        return res