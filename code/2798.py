'''
Author: lmio 2091319361@qq.com
Date: 2023-08-01 08:04:55
LastEditors: lmio 2091319361@qq.com
Description: 2798. 满足目标工作时长的员工数目
'''

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for hour in hours:
            if hour >= target:
                res += 1
        return res