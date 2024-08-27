'''
Author: lmio 2091319361@qq.com
Date: 2024-03-17 10:31:24
LastEditors: lmio 2091319361@qq.com
Description: 100248. 字符串及其反转中是否存在同一子字符串
'''

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        mm = set()
        s = list(s)
        for i in range(1, len(s)):
            mm.add(f'{s[i-1]}{s[i]}')
            if f'{s[i]}{s[i-1]}' in mm:
                return True
        return False