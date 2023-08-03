'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 09:18:03
LastEditors: lmio 2091319361@qq.com
Description: 面试题 01.06. 字符串压缩
'''

class Solution:
    def compressString(self, S: str) -> str:
        res = ''
        i = 0
        while i < len(S):
            ch = S[i]
            res += ch
            cnt = 1
            i += 1
            while i < len(S) and S[i] == ch:
                cnt += 1
                i += 1
            res += str(cnt)
        return res if len(res) < len(S) else S