from collections import defaultdict

n, L, R = list(map(int, input().split(" ")))
g = defaultdict(list)
for x in range(2, n+1):
    y = int(input())
    g[x].append(y)
    g[y].append(x)
res = 0
def dfs(x: int, fa: int, deep: int):
    global res
    if deep > R:
        return
    if deep >= L:
        res += deep
    for y in g[x]:
        if y != fa:
            dfs(y, x, deep+1)
for i in range(1, n+1):
    dfs(i, -1, 0)
print(res//2)