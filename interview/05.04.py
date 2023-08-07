'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 20:51:46
LastEditors: lmio 2091319361@qq.com
Description: 面试题 05.04. 下一个数
'''

from typing import List


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        # 1特判
        if num == 1:
            return [2, -1]
        # 例如0001 0111 -> 0001 1011
        def next_combo(num):
            # 获取最低位1的位权 0000 0001
            t = num & -num
            # 将最低位的1进一位 0001 1000
            y = num + t
            # num & ~y 获取发生进位的1的序列 0000 0111
            # (num & ~y)//t 将发生进位的最低位1挪到最右边，再向右移动一位，保证1的数目不变 0000 0011
            larger = (num & ~y)//t >> 1
            # 两个结果取或 0001 1011
            return larger|y
        more=next_combo(num)
        less=~next_combo(~num)
        if more>2147483647:
            more=-1
        if less==0:
            less=-1
        return [more,less]