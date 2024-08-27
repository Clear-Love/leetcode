'''
Author: lmio 2091319361@qq.com
Date: 2024-03-08 14:04:04
LastEditors: lmio 2091319361@qq.com
Description: 2834. 找出美丽数组的最小和
'''

MOD = 10**9+7
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mid = min(n, target//2)
        return ((mid*(1+mid)+(n-mid)*(2*target+n-mid)))%MOD/2