'''
Author: lmio 2091319361@qq.com
Date: 2024-05-29 20:13:23
LastEditors: lmio 2091319361@qq.com
Description: 2023次方
'''

import math

def f(n):
    cnt=0
    for i in range(1,n+1):
        if math.gcd(i,n)==1:
            cnt+=1
    return cnt

up = 2023
p = f(2023)

# 欧拉定理
for down in range(2022, 2, -1):
    up = pow(down, up, p)
print(pow(2,up,2023))