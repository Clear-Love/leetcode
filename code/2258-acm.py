from typing import List, Tuple


f=open("user.out",'w')
while True:
    try:
        row = input()[2:-2].split('],[')
        grid = []
        for r in row:
            grid.append(list(map(int, r.split(','))))
        m, n = len(grid), len(grid[0])
        def bfs(q: List[Tuple[int, int]]) -> (int, int, int):
            time = [[-1] * n for _ in range(m)]
            for i, j in q:
                time[i][j] = 0
            t = 1
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and time[x][y] < 0:
                            time[x][y] = t
                            q.append((x, y))
                t += 1
            return time[-1][-1], time[-1][-2], time[-2][-1]

        man_to_house_time, m1, m2 = bfs([(0, 0)])
        if man_to_house_time < 0:
            print(-1, file=f)  # 人无法到终点
            continue 
        fire_to_house_time, f1, f2 = bfs([(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 1])
        if fire_to_house_time < 0:
            print(10**9, file=f)  # 火无法到终点
            continue
        ans = fire_to_house_time - man_to_house_time
        if ans < 0:
            print(-1, file=f)  # 火比人先到终点
            continue
        if m1 < 0 or m2 < 0 or f1 - m1 == f2 - m2 == ans:
            print(ans-1, file=f)  # 火只会跟在人的后面，在到达终点前，人和火不能重合
            continue
        print(ans, file=f)  # 人和火可以同时到终点
    except:
        f.close()
        exit(0)