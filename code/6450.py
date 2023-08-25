'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 10:47:12
LastEditors: lmio 2091319361@qq.com
Description: 6450. k-avoiding 数组的最小总和
'''

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = 0
        visited = set()
        i = 1
        cnt = 0
        while cnt < n:
            if k-i not in visited:
                res += i
                cnt += 1
                visited.add(i)
            i += 1
        return res