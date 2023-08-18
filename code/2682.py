'''
Author: lmio 2091319361@qq.com
Date: 2023-08-16 20:02:09
LastEditors: lmio 2091319361@qq.com
Description: 2682. 找出转圈游戏输家
'''

from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        def next(i: int) ->int:
            return i%n
        arr = [False]*n
        i = 0
        cnt = 1
        while not arr[i]:
            arr[i] = True
            i = next(i+cnt*k)
            cnt += 1
        return [i+1 for i, v in enumerate(arr) if not v]