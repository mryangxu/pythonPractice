'''
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
'''
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):

    # 字符串先转为时间
    date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    # 匹配UTC中的时间信息
    hours = re.match(r'^UTC(\+|-)(\d+):', tz_str)

    # 组装hours参数
    if hours.group(1) == '+':
        hours_arg = int(hours.group(2))
    else:
        hours_arg = -int(hours.group(2))

    # 创建时区
    tz_utc = timezone(timedelta(hours=hours_arg))

    # 根据时区转换成UTC时间
    dt = date.replace(tzinfo=tz_utc)

    # 转成时间戳
    return dt.timestamp()


    pass

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')