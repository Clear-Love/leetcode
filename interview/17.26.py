'''
Author: lmio 2091319361@qq.com
Date: 2023-08-31 18:46:09
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.26. 稀疏相似度
'''

from typing import List


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        n = len(docs)
        res = []
        for i in range(n):
            l1 = len(docs[i])
            doc = set(docs[i])
            for j in range(i+1, n):
                l2 = len(docs[j])
                intersection = 0
                union = l1 + l2
                for v in docs[j]:
                    if v in doc:
                        union -= 1
                        intersection += 1
                if intersection > 0:
                    res.append(f'{i},{j}: {format(intersection/union, ".4f")}')
        return res