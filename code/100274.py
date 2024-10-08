'''
Author: lmio 2091319361@qq.com
Date: 2024-05-12 10:34:40
LastEditors: lmio 2091319361@qq.com
Description: 100274. 从魔法师身上吸取的最大能量
'''

from typing import List

#在神秘的地牢中，n 个魔法师站成一排。每个魔法师都拥有一个属性，这个属性可以给你提供能量。有些魔法师可能会给你负能量，即从你身上吸取能量。
#你被施加了一种诅咒，当你从魔法师 i 处吸收能量后，你将被立即传送到魔法师 (i + k) 处。这一过程将重复进行，直到你到达一个不存在 (i + k) 的魔法师为止。
#换句话说，你将选择一个起点，然后以 k 为间隔跳跃，直到到达魔法师序列的末端，在过程中吸收所有的能量。
#给定一个数组 energy 和一个整数k，返回你能获得的 最大 能量
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        for i in range(k):
            dp[i] = energy[i]
        for i in range(k, n):
            dp[i] = max(energy[i], dp[i-k]+energy[i])
        return max(dp[-k:])