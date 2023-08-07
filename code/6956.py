'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 22:45:56
LastEditors: lmio 2091319361@qq.com
Description: 6956. 使循环数组所有元素相等的最少秒数
'''

from collections import Counter
from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        cnts = Counter(nums)
        most = cnts.most_common()
        indices = []
        cnt = most[0][1]
        for i in range(len(most)):
            if most[i][1] != cnt:
                break
            indices.append([j for j, x in enumerate(nums) if x == most[i][0]])
        res = float('inf')
        for inds in indices:
            ans = 0
            j = -1
            for i in range(len(nums)):
                if j+1 < len(inds) and i == inds[j+1]:
                    j += 1
                elif i < inds[0]:
                    ans = max(ans, min(inds[0]-i, n - (inds[-1]-i)))
                elif inds[0] < i < inds[-1]:
                    ans = max(ans, min(i - inds[j], inds[j+1]-i))
                else:
                    ans = max(ans, min(i - inds[-1], n - (i-inds[0])))
            res = min(res, ans)
        return res