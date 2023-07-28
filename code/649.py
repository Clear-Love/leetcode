'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 16:16:30
LastEditors: lmio 2091319361@qq.com
Description: 649. Dota2 参议院
'''

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.popleft()
            dire.popleft()
        
        return "Radiant" if radiant else "Dire"