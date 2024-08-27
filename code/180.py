'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 18:19:29
LastEditors: lmio 2091319361@qq.com
Description: 180. 连续出现的数字
'''

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    res = set()
    curr = ""
    cnt = 0
    for i in logs["num"]:
        if (i == curr):
            cnt += 1
            if (cnt >= 3):
                res.add(i)
        else:
            curr = i
            cnt = 1
    return pd.DataFrame(res, columns=["ConsecutiveNums"]) if len(res) > 0 else pd.DataFrame(columns=["ConsecutiveNums"])
