'''
Author: lmio 2091319361@qq.com
Date: 2024-04-06 19:01:01
LastEditors: lmio 2091319361@qq.com
Description: 费用报销
'''
from itertools import accumulate


days=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

alldays = list(accumulate(days))

n, M, k = map(int,input().split())
dp=[0]*366

for i in range(n):
    month,day,value = map(int,input().split())
    dp[alldays[month-1]+day] = max(dp[alldays[month-1]+day],value)#今年的第n天的票据值为当天票据的最大值


for i in range(1,366):
    pre = max(0, i-k)#保证不小于零
    if dp[i] + dp[pre] <= M:
        dp[i] = max(dp[i-1], dp[i] + dp[pre])
    else:
        dp[i] = dp[i-1]
print(dp[-1])