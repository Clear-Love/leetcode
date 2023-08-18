'''
Author: lmio 2091319361@qq.com
Date: 2023-08-15 21:59:12
LastEditors: lmio 2091319361@qq.com
Description: 833. 字符串中的查找与替换
'''

from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        offset = 0
        strs = list(zip(indices, sources, targets))
        strs.sort(key=lambda x: x[0])
        for indice, source, target in strs:
            n, m = len(source), len(target)
            indice = indice + offset
            if s.startswith(source, indice):
                s = s[:indice] + target + s[indice+n:]
                offset += m-n
        return s