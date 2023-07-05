'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 22:31:07
LastEditors: lmio 2091319361@qq.com
Description: 
'''

from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for str in strs:
        sorted_word = ''.join(sorted(str))
        groups[sorted_word].append(str)
    return list(groups.values())