'''
Author: lmio 2091319361@qq.com
Date: 2023-08-29 16:44:46
LastEditors: lmio 2091319361@qq.com
Description: 823. 带因子的二叉树
'''

from math import sqrt
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10**9+7
        cnts = {}
        m = set(arr)
        res = 0
        for v in arr:
            cnts[v] = 1
            i = 0
            while arr[i] <= sqrt(v):
                tar = v/arr[i]
                if tar in m:
                    c = (cnts[arr[i]]*cnts[tar])%MOD
                    if arr[i] == tar:
                        cnts[v] += c
                    else:
                        cnts[v] += 2*c
                i += 1
            res += cnts[v]%MOD
        return res%MOD