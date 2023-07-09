'''
Author: lmio 2091319361@qq.com
Date: 2023-07-09 11:35:28
LastEditors: lmio 2091319361@qq.com
Description: 6919. 使数组中的所有元素都等于零
'''

from typing import List


def checkArray(nums: List[int], k: int) -> bool:
    n = len(nums)
    d = [0] * n
    last = 0
    for i, num in enumerate(nums):
        if i >= k:
            # 减去之前的子数组
            last -= d[i-k]
        v = num - last
        if v < 0: 
            return False
        d[i] = v
        last += v
    for i in range(n-k+1, n):
        if d[i]: return False
    return True