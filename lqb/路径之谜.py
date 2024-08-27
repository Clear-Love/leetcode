import sys
# 请在此输入您的代码
n = int(input())
upCnt = list(map(int, input().split()))
leftCnt = list(map(int, input().split()))

vis = set()
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

res = []

def dfs(x: int, y: int):
    global res, vis
    res.append(str(x*n+y))
    vis.add((x, y))
    upCnt[y] -= 1
    leftCnt[x] -= 1

    if leftCnt[x] < 0 or upCnt[y] < 0:
        return
    if leftCnt[x] == 0:
        # 不能再回到这一行
        for i in range(x):
            if leftCnt[i] > 0:
                return
    if upCnt[y] == 0:
        # 不能再回到这一列
        for i in range(y):
            if upCnt[i] > 0:
                return
    if (x, y) == (n-1, n-1):
        if sum(leftCnt) == 0 and sum(upCnt) == 0:
            print(' '.join(res))
            sys.exit(0) # 找到一个就退出
        else:
            return
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in vis:
            dfs(nx, ny) 
            res.pop()
            upCnt[ny] += 1
            leftCnt[nx] += 1
            vis.remove((nx, ny))
    return

dfs(0, 0)
