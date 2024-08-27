M = 50
mat = [[0 for _ in range(M)] for _ in range(M)]
flag = False
v = 1
for i in range(M):
    for j in range(i+1):
        # 右上到左下
        if flag:
            mat[j][i-j] = v
        # 左下到右上
        else:
            mat[i-j][j] = v
        v += 1
    flag = not flag

print(mat[19][19])