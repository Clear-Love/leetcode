'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 20:18:57
LastEditors: lmio 2091319361@qq.com
Description: 185. 部门工资前三高的所有员工
'''
import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    table = pd.merge(
        employee,
        department,
        how='left',
        left_on='departmentId',
        right_on='id'
    )
    table.rename(columns={'name_x': 'Employee',
                 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)
    table['rank'] = table.groupby('Department')['Salary'].rank(method='dense', ascending=False)
    res = table[table['rank'] <= 3]
    return res[['Department', 'Employee', 'Salary']]
