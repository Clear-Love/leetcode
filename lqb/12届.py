from collections import defaultdict
from fractions import Fraction
from functools import cache
import heapq
import math

from sympy import divisors


def loop(c: int):
    cnts = [c]*10
    i = 1
    while True:
        tmp = i
        while tmp:
            v = tmp%10
            tmp = tmp // 10
            if not cnts[v]:
                print(i if not tmp else i-1)
                return
            cnts[v] -= 1
        i += 1

# loop(2021)

# t1: 3180

s = set()
points = [(x, y) for x in range(20) for y in range(21)]


def count_lines(points):
    slopes = set()
    m = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dx, dy = x2 - x1, y2 - y1
            if dx == 0:
                # tan90 特殊判定
                m.add(x1)
                continue
            else:
                slope = Fraction(dy, dx)
            # 截距
            intercept = y1 - slope * x1
            line = (slope, intercept)
            slopes.add(line)
    return len(slopes) + len(m)
# print(count_lines(points))

# t2: 40257

@cache
def dfs(i: int, v: int) -> int:
    if i == 3:
        return 1
    res = 0
    for j in divisors(v, generator=True):
        res += dfs(i+1, v//j)
    return res

# 2021041820210418
#print(dfs(1, 2021041820210418))

# t3: 2430

def minPath() ->int:
    vis = set()
    q= [(0, 1)]
    while q:
        l, node = heapq.heappop(q)
        if node in vis:
            continue
        if node == 23:
            return l
        vis.add(node)
        for nex in range(node+1, node+22):
            cost = math.lcm(node, nex)
            heapq.heappush(q, (l+cost, nex))

# print(minPath())

# t4: 10266837

def count():
    g = defaultdict(list)
    for i in range(1, 22):
        for j in range(i+1, 22):
            if math.gcd(i, j) == 1:
                g[i].append(j)
                g[j].append(i)
    key = (1 << 22)-1
    @cache
    def dfs(i:int, mask: int) ->int:
        if i == 1 and mask == key:
            return 1
        # 访问过
        if mask & (1 << i):
            return 0
        mask |= (1 << i)
        res = 0
        for j in g[i]:
            res += dfs(j, mask)
        return res
    return dfs(1, 1)
# print(count())
# t5: 881012367360

# 空间

# print(256*1024*1024*8//32)