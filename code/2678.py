'''
Author: lmio 2091319361@qq.com
Date: 2023-10-23 11:48:11
LastEditors: lmio 2091319361@qq.com
Description: 2678. 老人的数目
'''

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for detail in details:
            if int(detail[-4:-2]) > 60:
                res += 1
        return res