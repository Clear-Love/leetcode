f = [[[0 for _ in range(2030)] for _ in range(11)] for _ in range(2030)]
f[0][0][0] = 1

for i in range(1, 2023):
    for j in range(11):
        for v in range(2023):
            if v - i >= 0 and j >= 1:
                f[i][j][v] = f[i - 1][j - 1][v - i]
            f[i][j][v] += f[i - 1][j][v]

print(f[2022][10][2022])