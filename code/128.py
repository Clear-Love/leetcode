'''
Author: lmio 2091319361@qq.com
Date: 2023-07-06 20:18:36
LastEditors: lmio 2091319361@qq.com
Description: 128. 最长连续序列
'''

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    res = 0
    nMap = {}
    for num in nums:
        l = 1
        if num in nMap:
            continue
        else:
            prev, next = nMap.get(num-1, 0), nMap.get(num+1, 0)
            l = prev + next + 1
            nMap[num-prev] = l
            nMap[num] = l
            nMap[num+next] = l
        res = max(res, l)
    return res

print(longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))