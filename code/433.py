'''
Author: lmio 2091319361@qq.com
Date: 2023-07-13 21:50:55
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque()
        queue.append([startGene, 0])
        while queue:
            tmp, step = queue.popleft()
            if tmp == endGene:
                return step
            for i, v in enumerate(tmp):
                for k in 'ATCG':
                    if v == k: 
                        continue
                    val = tmp[:i] + k + tmp[i+1:]
                    if val in bank:
                        bank.remove(val)
                        queue.append([val, step+1])
        return -1