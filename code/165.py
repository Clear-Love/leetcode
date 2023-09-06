'''
Author: lmio 2091319361@qq.com
Date: 2023-09-01 15:28:57
LastEditors: lmio 2091319361@qq.com
Description: 165. 比较版本号
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        l1, l2 = len(v1), len(v2)
        n = min(l1, l2)
        for i in range(n):
            if v1[i] == v2[i]:
                continue
            elif v1[i] > v2[i]:
                return 1
            else:
                return -1
        if l1 == l2:
            return 0
        elif l1 > l2:
            if all(v1[i] == 0 for i in range(n, l1)):
                return 0
            return 1
        else:
            if all(v2[i] == 0 for i in range(n, l2)):
                return 0
            return -1