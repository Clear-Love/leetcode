'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 18:03:08
LastEditors: lmio 2091319361@qq.com
Description: 2379. 得到 K 个黑块的最少涂色次数
'''

from typing import Counter


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnts = Counter(blocks[:k])
        res = k-cnts['B']
        left, right = 0, k
        n = len(blocks)
        while right < n:
            cnts[blocks[right]] += 1
            cnts[blocks[left]] -= 1
            res = min(res, k-cnts['B'])
            left += 1
            right += 1
        return res