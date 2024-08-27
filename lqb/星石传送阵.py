'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 09:09:33
LastEditors: lmio 2091319361@qq.com
Description: 星石传送阵
'''
from collections import defaultdict, deque
from math import inf
import sys


MX = 10**4+5

primes = []
is_prime = [True]*(MX+1)

for i in range(2, MX+1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*i, MX+1, i):
            is_prime[j] = False

# 分解质因数 
def get_prime_divisors_sum(n: int):
    res = 0
    for p in primes:
        if n <= 1:
            break
        while n%p == 0:
            res += p
            n //= p
    if n > 1:
        res += n
    return res

n, a, b = list(map(int, input().split()))
vals = [0] + list(map(int, input().split()))

g = defaultdict(list)

# 添加虚拟点，到虚拟点的边权为1，从虚拟点放回为0
for i in range(1, n+1):
    fx = (get_prime_divisors_sum(vals[i])%n)+1
    g[i].append((fx, 1))
    g[fx].append((i, 1))
    g[n+1+fx].append((i, 0))
    g[i].append((n+1+fx, 1))

q = deque([(0, a)])
vis = set()
dis = defaultdict(lambda: inf)
dis[a] = 0

# 0-1BFS
while q:
    d, x = q.popleft()
    if x in vis:
        continue
    if x == b:
        print(d)
        sys.exit(0)
    vis.add(x)
    for y, w in g[x]:
        if dis[y] > dis[x] + w:
            dis[y] = dis[x] + w
            if w == 0:
                q.appendleft((dis[y], y))
            else:
                q.append((dis[y], y))

print(-1)