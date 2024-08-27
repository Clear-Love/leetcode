'''
Author: lmio 2091319361@qq.com
Date: 2024-04-12 19:56:00
LastEditors: lmio 2091319361@qq.com
Description: 子矩阵
'''

from collections import deque


MOD = 998244353
n, m, a, b = list(map(int, input().split()))
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

min_row = [[0 for _ in range(m)] for _ in range(n)]
max_row = [[0 for _ in range(m)] for _ in range(n)]
# 得到某一行 长度为b的最小值
def get_min(i: int):
    # 得到最小值， 维护一个单调递增的队列
    q = deque()
    for j, num in enumerate(mat[i]):
        while q and q[0] <= j-b:
            q.popleft()
        while q and mat[i][q[-1]] > num:
            q.pop()
        q.append(j)
        min_row[i][j] = mat[i][q[0]]

# 得到某一行 长度为b的最大值
def get_max(i: int):
    # 得到最小值， 维护一个单调递减的队列
    q = deque()
    for j, num in enumerate(mat[i]):
        while q and q[0] <= j-b:
            q.popleft()
        while q and mat[i][q[-1]] < num:
            q.pop()
        q.append(j)
        max_row[i][j] = mat[i][q[0]]
for i in range(n):
    get_min(i)
    get_max(i)

res = 0
for j in range(b-1, m):
    max_q = deque()
    min_q = deque()
    for i in range(a-1):
        while max_q and max_row[max_q[-1]][j] < max_row[i][j]:
            max_q.pop()
        while max_q and max_row[min_q[-1]][j] > min_row[i][j]:
            min_q.pop()
        max_q.append(i)
        min_q.append(i)
    for i in range(a-1, n):
        while max_q and max_q[0] <= i-a:
            max_q.popleft()
        while min_q and min_q[0] <= i-a:
            min_q.popleft()
        while max_q and max_row[max_q[-1]][j] < max_row[i][j]:
            max_q.pop()
        while max_q and max_row[min_q[-1]][j] > min_row[i][j]:
            min_q.pop()
        max_q.append(i)
        min_q.append(i)
        res += max_row[max_q[0]][j]*min_row[min_q[0]][j]%MOD

print(res)