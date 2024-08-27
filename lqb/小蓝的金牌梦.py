'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 11:06:31
LastEditors: lmio 2091319361@qq.com
Description: 小蓝的金牌梦
'''
from math import inf

n = int(input())
nums = list(map(int, input().split()))

MX = n+1

is_prime = [True]*MX
primes = []

for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i*i, MX, i):
            is_prime[j] = False

preSum = [0]*(n+1)

for i in range(1, n+1):
    preSum[i] = preSum[i-1]+nums[i-1]

res = -inf

for p in primes:
    for i in range(p, n+1):
        res = max(res, preSum[i]-preSum[i-p])

print(res)