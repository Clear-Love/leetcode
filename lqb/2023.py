'''
Author: lmio 2091319361@qq.com
Date: 2024-04-09 18:17:45
LastEditors: lmio 2091319361@qq.com
Description: 2023
'''

start, end = 12345678, 98765432

arr = [3, 2, 0, 2]

def check(n: int):
    i = 0
    while n:
        if i == 4:
            return True
        n, v = divmod(n, 10)
        if v == arr[i]:
            i += 1
res = 0
for num in range(start, end+1):
    if not check(num):
        res += 1
print(res)