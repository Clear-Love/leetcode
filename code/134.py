'''
Author: lmio 2091319361@qq.com
Date: 2023-07-02 16:08:57
LastEditors: lmio 2091319361@qq.com
Description: 134. 加油站
'''
from typing import List

# 存在这样一个性质：
# 如果从加油站i不能到达加油站j
# 那么i~j之间的任何节点都不能到达加油站j
# 所以，下一次判断可以直接从加油站j开始

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    start = 0
    while start < len(gas):
        inx = start
        cnt = 0
        rgas = 0
        while cnt < len(gas):
            rgas = rgas + gas[inx] - cost[inx]
            if rgas < 0:
                break
            inx = (inx + 1) % len(gas)
            cnt += 1
        if cnt == len(gas):
            return start
        else:
            start += cnt + 1
    return -1


# 还存在一种贪心性质：
# 无论如何，选择距离剩余油最少的加油站最远的的总是最优解
def canCompleteCircuitII(gas, cost):
    length = len(gas)
    spare = 0
    # 最小剩余油
    min_spare = float('inf')
    res = 0

    for i in range(length):
        spare += gas[i] - cost[i]
        if spare < min_spare:
            min_spare = spare
            res = i

    return -1 if spare < 0 else (res + 1) % length
