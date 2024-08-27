'''
Author: lmio 2091319361@qq.com
Date: 2024-03-18 15:52:20
LastEditors: lmio 2091319361@qq.com
Description: LCP 30. 魔塔游戏
'''

import heapq
from typing import List


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        arr = []
        q = []
        hp = 1
        cnt = 0
        for num in nums:
            if num < 0:
                heapq.heappush(q, num)
            if hp + num <= 0:
                t = heapq.heappop(q)
                arr.append(t)
                cnt += 1
                hp += num-t
            else:
                hp += num
        return -1 if (hp+sum(arr)) <= 0 else cnt

print(Solution().magicTower([100, 100,100,-250,-60,-140,-50,-50,100,150]))