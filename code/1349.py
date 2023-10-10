'''
Author: lmio 2091319361@qq.com
Date: 2023-09-28 21:01:31
LastEditors: lmio 2091319361@qq.com
Description: 1349. 参加考试的最大学生数
'''

from typing import List


from functools import reduce
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0]),
        dp = [[0]*(1 << n) for _ in range(m+1)] 
        a = [reduce(lambda x,y:x|1<<y,[0]+[j for j in range(n) if seats[i][j]=='#'])  for i in range(m)]
        for row in range(m)[::-1]:
            for j in range(1 << n):
                if not j & j<<1 and not j&j>>1 and not j & a[row]: 
                    for k in range(1 << n):
                        if not j&k<<1 and not j&k>>1:
                            dp[row][j] = max(dp[row][j], dp[row+1][k] + bin(j).count('1'))
        return max(dp[0])