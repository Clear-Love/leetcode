'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 16:10:11
LastEditors: lmio 2091319361@qq.com
Description: 933. 最近的请求次数
'''

class RecentCounter:

    def __init__(self):
        self.time = []

    def ping(self, t: int) -> int:
        self.time.append(t)
        while t - self.time[0] > 3000:
            self.time.pop(0)
        return len(self.time)