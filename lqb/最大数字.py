n, ca, cb = list(map(int, input().split()))
n = list(str(n))

res = 0

def dfs(i: int, a: int, b: int):
    global n, res
    if i >= len(n) or a == b == 0:
        return
    tmp = n[i]
    # 使用a方法
    v = int(n[i])
    ta = a
    while ta:
        if (v+1)%10 > v:
            v += 1
        ta -= 1
    n[i] = str(v)
    res = max(res, int(''.join(n)))
    dfs(i+1, ta, b)
    # 使用b方法
    n[i] = tmp
    v = int(n[i])
    if v < b:
        n[i] = str("9")
        b -= (v+1)
        res = max(res, int(''.join(n)))
        dfs(i+1, a, b)
    n[i] = tmp
dfs(0, ca, cb)
print(res)