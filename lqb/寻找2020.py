'''
Author: lmio 2091319361@qq.com
Date: 2024-04-11 19:22:19
LastEditors: lmio 2091319361@qq.com
Description: 寻找2020
'''

mat = []
n = 300
with open('./lqb/2020.txt', 'r') as f:
    for line in f:
        mat.append(line[0:300])
n = 300
ans = 0
for i in range(n):
    for j in range(n):
        if i+3 < n and mat[i][j] == '2' and mat[i+1][j] == '0' and mat[i+2][j] == '2' and mat[i+3][j] == '0':
            ans += 1
        if j+3 < n and mat[i][j] == '2' and mat[i][j+1] == '0' and mat[i][j+2] == '2' and mat[i][j+3] == '0':
            ans += 1
        if i+3 < n and j+3 < n and mat[i][j] == '2' and mat[i+1][j+1] == '0' and mat[i+2][j+2] == '2' and mat[i+3][j+3] == '0':
            ans += 1
print(ans)