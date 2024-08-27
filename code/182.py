'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 19:18:02
LastEditors: lmio 2091319361@qq.com
Description: 182. 查找重复的电子邮箱
'''

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby('email').size().reset_index(name='count')
    df = df[df['count'] > 1]
    return df['email']