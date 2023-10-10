'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 17:56:50
LastEditors: lmio 2091319361@qq.com
Description: 1343. 大小为 K 且平均值大于等于阈值的子数组数目
'''

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        res = 0 if s/k < threshold else 1
        left, right = 0, k
        n = len(arr)
        while right < n:
            s += arr[right]-arr[left]
            if s/k >= threshold:
                res += 1
            left += 1
            right += 1
        return res