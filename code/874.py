'''
Author: lmio 2091319361@qq.com
Date: 2023-07-19 21:42:40
LastEditors: lmio 2091319361@qq.com
Description: 874. 模拟行走机器人
'''
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obst = set()
        for v in obstacles:
            obst.add((v[0], v[1]))
        pos = (0, 0)
        faces = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        face = 0
        res = 0
        def run(step: int):
            nonlocal pos
            dx, dy = faces[face]
            for _ in range(step):
                pos = (pos[0]+dx, pos[1]+dy)
                if pos in obst:
                    pos = (pos[0]-dx, pos[1]-dy)
                    break
                
        for cmd in commands:
            if cmd == -2:
                face = (face + 1)%4
            elif cmd == -1:
                face = (face - 1)%4
            else:
                run(cmd)
                res = max(res, pos[0]*pos[0] + pos[1]*pos[1])
        return res