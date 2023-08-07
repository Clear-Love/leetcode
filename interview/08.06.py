'''
Author: lmio 2091319361@qq.com
Date: 2023-08-07 19:52:51
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.06. 汉诺塔问题
'''

from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        # 把A上面的n-1个盘子通过B移动到A
        def move(n: int, A: List[int], B: List[int], C: List[int]):
            if n == 1:
                C.append(A.pop())
                return
            move(n-1, A, C, B)
            C.append(A.pop())
            move(n-1, B, A, C)
        move(len(A), A, B, C)
        return C