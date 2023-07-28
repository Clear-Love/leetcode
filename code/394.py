'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 14:47:05
LastEditors: lmio 2091319361@qq.com
Description: 394. 字符串解码
'''
class Solution:
    def decodeString(self, s: str) -> str:
        ptr = 0
        def dfs():
            nonlocal ptr
            res, repCnt = "", 0
            while ptr < len(s):
                if '0' <= s[ptr] <= '9':
                    repCnt = repCnt * 10 + int(s[ptr])
                elif s[ptr] == '[':
                    ptr += 1
                    res += repCnt * dfs()
                    repCnt = 0
                elif s[ptr] == ']':
                    return res
                else:
                    res += s[ptr]
                ptr += 1
            return res
        return dfs()