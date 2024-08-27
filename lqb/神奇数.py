'''
Author: lmio 2091319361@qq.com
Date: 2024-05-30 18:50:16
LastEditors: lmio 2091319361@qq.com
Description: 神奇数
'''
from functools import lru_cache

l = int(input())
r = int(input())

MOD = 998244353

# isLimit: 是否受到限制 isNum: 前面是否是数字, preSum: 前面数字的和, i: 第i位数字，可以跳过
def calc(num: int) -> int:
    s = str(num)
    n = len(s)
    @lru_cache(None)
    def dfs(i: int, preSum: int, isLimit: bool, isNum: bool) -> int:
        end = int(s[i]) if isLimit else 9
        # 最后一位
        if i == n-1:
            return sum(1 for i in range(1, end+1) if preSum%i == 0)
        start = 0 if isNum else 1
        res = 0
        if not isNum:
            # 忽略这一位, 少一位不再限制，
            res += dfs(i+1, preSum, False, isLimit)%MOD
        for x in range(start, end+1):
            res += dfs(i+1, preSum+x, isLimit and x == end, True)%MOD
        return res%MOD
    return dfs(0, 0, True, False)

print((calc(r) - calc(l-1))%MOD)