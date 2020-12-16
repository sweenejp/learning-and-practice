import datetime


def far_away(duration):
    return duration + datetime.datetime.now()


five_hours = datetime.timedelta(hours=5)
print(five_hours)
print(datetime.datetime.now())
print(far_away(five_hours))

today = datetime.date.today()
midnight = datetime.time()
print(today)
print(midnight)
today_at_midnight = datetime.datetime.combine(today, midnight)
print(today_at_midnight)

print(datetime.timedelta.total_seconds(five_hours))
time1 = datetime.datetime(2020, 4, 8, 12, 0, 0)
time2 = datetime.datetime(2020, 4, 8, 12, 30, 0)
print(time2 - time1)


def minutes(t1, t2):
    difference = t2 - t1
    return round(datetime.timedelta.total_seconds(difference) / 60)


print(minutes(time1, time2))
