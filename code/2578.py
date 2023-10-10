'''
Author: lmio 2091319361@qq.com
Date: 2023-10-09 23:14:13
LastEditors: lmio 2091319361@qq.com
Description: 2578. 最小和分割
'''

class Solution:
    def splitNum(self, num: int) -> int:
        stnum = "".join(sorted(str(num)))
        num1, num2 = int(stnum[::2]), int(stnum[1::2])
        return num1 + num2