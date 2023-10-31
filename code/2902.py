'''
Author: lmio 2091319361@qq.com
Date: 2023-10-20 14:52:23
LastEditors: lmio 2091319361@qq.com
Description: 2902. 和带限制的子多重集合的数目
'''

from collections import Counter
from typing import List


class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        total = sum(nums)
        if l > total:
            return 0
        r = min(r, total)
        cnt = Counter(nums)
        f = [cnt[0] + 1] + [0] * r
        del cnt[0]
        s = 0
        for x, c in cnt.items():
            new_f = f.copy()
            s = min(s + x * c, r)  # 到目前为止，能选的元素和至多为 s
            for j in range(x, s + 1):  # 把循环上界从 r 改成 s，能快一倍
                new_f[j] += new_f[j - x]
                if j >= (c + 1) * x:
                    new_f[j] -= f[j - (c + 1) * x]
                new_f[j] %= MOD
            f = new_f
        return sum(f[l:]) % MOD