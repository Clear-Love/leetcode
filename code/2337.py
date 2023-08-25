'''
Author: lmio 2091319361@qq.com
Date: 2023-08-21 20:14:09
LastEditors: lmio 2091319361@qq.com
Description: 2337. 移动片段得到字符串
'''

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        j = 0
        for i, ch in enumerate(start):
            if ch == '_':
                continue
            while target[j] == '_':
                j += 1
            if ch == 'L' and i < j:
                return False
            if ch == 'R' and i > j:
                return False
            j += 1
        return True