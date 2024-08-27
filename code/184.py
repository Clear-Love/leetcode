'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 19:46:29
LastEditors: lmio 2091319361@qq.com
Description: 184. 部门工资最高的员工
'''

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    table = pd.merge(
        employee,
        department,
        how='left',
        left_on='departmentId',
        right_on='id'        
    )
    table.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'}, inplace=True)
    max_salary = table.groupby('Department')['Salary'].transform('max')
    res = table[table['Salary'] == max_salary]
    return res[['Department', 'Employee', 'Salary']]