import datetime

now = datetime.datetime.now()
today = datetime.datetime(
    year=now.year,
    month=now.month,
    day=now.day,
    hour=0,
    minute=0,
    second=0,
)

print(now)
print(today)

delta = datetime.timedelta(days=1)
print(delta)
print(now + delta)
