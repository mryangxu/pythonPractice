from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2020, 2, 2, 20, 2, 20)

print(dt)

# datetime 转为 timestamp
print(dt.timestamp())

# timestamp 转为 datetime
t = 1429417200
print(datetime.fromtimestamp(t))

# 直接转为utc标准时间
print(datetime.utcfromtimestamp(t))

# str转为datetime
cday = datetime.strptime('2020-3-11 17:12:12', '%Y-%m-%d %H:%M:%S')
print(cday)
print(type(cday))

# datetime 转 str
print(now.strftime('%Y-%m-%d %H:%I'))

# datetime 加减
from datetime import timedelta
print(now + timedelta(days=1))
print(now - timedelta(hours=1))
print(now - timedelta(minutes=1))
print(now - timedelta(seconds=10, hours=1))

# 本地时间转为utc时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00

dt = now.replace(tzinfo=tz_utc_8) #强制设置为 UTC+8:00

print(dt)

# 时区转换

# 拿到utc时间，并强制设置时区为UTC+0：00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 转为北京时区
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 转为东京时区
dj_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(dj_dt)
# 将北京时区转为东京时区
dj_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
