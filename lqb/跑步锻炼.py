'''
Author: lmio 2091319361@qq.com
Date: 2024-04-11 20:04:00
LastEditors: lmio 2091319361@qq.com
Description: 
'''

from datetime import datetime, timedelta

# 定义起始日期和结束日期
start_date = datetime(2000, 1, 1)
end_date = datetime(2020, 10, 1)

# 初始化小蓝的总跑步距离
res = 0

# 循环遍历每一天
current_date = start_date
while current_date <= end_date:
    # 判断是否是周一或者月初
    if current_date.weekday() == 0 or current_date.day == 1:
        # 如果是周一或者月初，跑2千米
        res += 2
    else:
        # 否则跑1千米
        res += 1
    # 增加一天
    current_date += timedelta(days=1)

print(res)