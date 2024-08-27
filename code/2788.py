'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 17:41:54
LastEditors: lmio 2091319361@qq.com
Description: 2788. 按分隔符拆分字符串
'''

from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            res.extend([s for s in word.split(separator) if s])
        return res