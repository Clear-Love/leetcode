'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 22:03:58
LastEditors: lmio 2091319361@qq.com
Description: 290. 单词规律
'''

def wordPattern(pattern: str, s: str) -> bool:
    s = s.split(' ')
    if len(pattern) != len(s):
        return False
    pTs = {}
    sTp = {}
    for i in range(len(pattern)):
        pi = pattern[i]
        si = s[i]
        if pi in pTs and si in sTp:
            if pTs[pi] != si:
                return False
        elif pi not in pTs and si not in sTp:
            pTs[pi] = si
            sTp[si] = pi
        else:
            return False
    return True