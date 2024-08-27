'''
Author: lmio 2091319361@qq.com
Date: 2024-05-28 18:59:50
LastEditors: lmio 2091319361@qq.com
Description: 分考场
'''

n = int(input())
m = int(input())

dis = [[False]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = list(map(int, input().split()))
    dis[x][y] = True
    dis[y][x] = True

rooms = [[] for _ in range(n)]
res = n

def dfs(i: int, roomCnt: int):
    global res, rooms, dis, n
    if roomCnt >= res:
        return
    if i == n+1:
        res = min(res, roomCnt)
        return
    for j in range(roomCnt):
        # 可以进入这个教室
        if all(not dis[x][i] for x in rooms[j]):
            rooms[j].append(i)
            dfs(i+1, roomCnt)
            # 回溯
            rooms[j].pop()
    # 当前所有教室无法进入，新建立一个教室
    rooms[roomCnt].append(i)
    dfs(i+1, roomCnt+1)
    rooms[roomCnt].pop()

dfs(1, 0)
print(res)