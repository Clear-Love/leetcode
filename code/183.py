'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 19:29:53
LastEditors: lmio 2091319361@qq.com
Description: 183. 从不订购的客户
'''

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    table = pd.merge(
        customers,
        orders,
        how='left',
        left_on='id',
        right_on='customerId'
    )
    res = table[table['customerId'].isnull()][['name']].rename('Customers')
    return res
