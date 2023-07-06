'''
Author: lmio 2091319361@qq.com
Date: 2023-07-06 20:14:18
LastEditors: lmio 2091319361@qq.com
Description: 219. 存在重复元素 II
'''

from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    nMap = {}
    for i, v in enumerate(nums):
        if v in nMap:
            if i - nMap[v] <= k:
                return True
            else:
                nMap[v] = i
        else:
            nMap[v] = i
    return False