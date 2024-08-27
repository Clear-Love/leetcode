'''
Author: lmio 2091319361@qq.com
Date: 2024-05-15 19:40:16
LastEditors: lmio 2091319361@qq.com
Description: 2522. 将字符串分割成值不超过 K 的子字符串
'''

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        v = 0
        res = 1
        for c in s:
            num = int(c)
            if num > k: # 如果当前数字大于k，无法找到任一分割使其和不超过k
                return -1
            v = v * 10 + int(c)
            if v > k: # 需要分割
                res += 1
                v = num
        return res