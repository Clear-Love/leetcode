'''
Author: lmio 2091319361@qq.com
Date: 2023-10-20 11:05:34
LastEditors: lmio 2091319361@qq.com
Description: 2525. 根据规则将箱子分类
'''


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        h = 10**4
        bulky = length >= h or width >= h or height >= h or length*width*height >= 10**9
        heavy = mass >= 100
        if bulky and heavy:
            return 'Both'
        elif not bulky and not heavy:
            return 'Neither'
        elif bulky:
            return 'Bulky'
        else:
            return 'Heavy'