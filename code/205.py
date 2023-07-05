'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 21:52:15
LastEditors: lmio 2091319361@qq.com
Description: 205. 同构字符串
'''

def isIsomorphic(s: str, t: str) -> bool:
    sTt = {}
    tTs = {}
    for i in range(len(t)):
        ti = t[i]
        si = s[i]
        if si in sTt and ti in tTs:
            if sTt[si] != ti:
                return False
        elif si not in sTt and ti not in tTs:
            sTt[si] = ti
            tTs[ti] = si
        else:
            return False
    return True