'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 18:54:56
LastEditors: lmio 2091319361@qq.com
Description: 181. 超过经理收入的员工
'''


import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_table = pd.merge(
        employee,
        employee,
        how='left',
        left_on='managerId',
        right_on='id'
    )
    result = merged_table.query('salary_x > salary_y')['name_x'].rename('Employee').to_frame()
    return result