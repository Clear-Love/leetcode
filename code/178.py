'''
Author: lmio 2091319361@qq.com
Date: 2024-01-20 18:06:28
LastEditors: lmio 2091319361@qq.com
Description: 178. 分数排名
'''

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score', 'rank']].sort_values('score', ascending=False)