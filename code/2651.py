'''
Author: lmio 2091319361@qq.com
Date: 2023-09-08 10:48:26
LastEditors: lmio 2091319361@qq.com
Description: 2651. 计算列车到站时间
'''

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime)%24