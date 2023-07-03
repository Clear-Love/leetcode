'''
Author: lmio 2091319361@qq.com
Date: 2023-07-03 22:29:27
LastEditors: lmio 2091319361@qq.com
Description: 68. 文本左右对齐
'''
import math
from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    length = 0
    res = []
    row = []
    def align() -> str:
        if len(row) == 1:
            return row[0].ljust(maxWidth)
        q, r = divmod(maxWidth - length, len(row)-1)
        for i in range(len(row)):
            row[i] += ' '*(q + (i < r))
        return ''.join(row).strip()
    
    for i in range(len(words)):
        if length + len(words[i]) + len(row)-1 >= maxWidth:
            res.append(align())
            row = [words[i]]
            length = len(words[i])
        else:
            length += len(words[i])
            row.append(words[i])
    res.append(' '.join(row).ljust(maxWidth))
    return res