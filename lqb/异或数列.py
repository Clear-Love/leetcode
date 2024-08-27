'''
Author: lmio 2091319361@qq.com
Date: 2024-04-03 01:28:56
LastEditors: lmio 2091319361@qq.com
Description: 异或数列
'''

from collections import defaultdict
from typing import List


keys = []
for i in range(32):
    keys.append(1 << (31-i))

T = int(input())
List
for _ in range(T):
    n, *nums = list(map(int, input().split(" ")))
    def win():
        cnts = defaultdict(int)
        for num in nums:
            for key in keys:
                if num&key:
                    cnts[key] += 1
        for key in keys:
            cnt = cnts[key]
            # 最高位个数为偶数，看次高位
            if not cnt or (cnt&1) == 0:
                continue
            if cnt == 1:
                return 1
            return 1 if n&1 else 0
        return 0
    print(win())