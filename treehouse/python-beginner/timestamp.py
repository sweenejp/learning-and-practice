import datetime


def timestamp_oldest(*args):
    a1 = []
    for arg in args:
        a1.append(arg)
    a1.sort()
    return datetime.datetime.fromtimestamp(a1[0])


a_long_time_ago = timestamp_oldest(10, 5446545, 22312, 96115, 23230)
print(a_long_time_ago)