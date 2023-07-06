'''
Author: lmio 2091319361@qq.com
Date: 2023-07-06 21:23:12
LastEditors: lmio 2091319361@qq.com
Description: 228. 汇总区间
'''

from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    if len(nums) == 0:
            return []
    sections =[[nums[0], nums[0]]]
    for i in range(1, len(nums)):
        if nums[i] - 1 == nums[i-1]:
            sections[-1][1] = nums[i]
        else:
            sections.append([nums[i], nums[i]])
    res = []
    for section in sections:
        if section[0] == section[1]:
            res.append(str(section[0]))
        else:
            res.append(str(section[0]) + '->' + str(section[1]))
    return res