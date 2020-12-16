import datetime

# note - these functions do exactly what the strftime and strptime methods
# already do. It was just practice

def to_string(dt):
    return datetime.datetime.strftime(dt, "%d %B %Y")


def from_string(date, strftime_format):
    return datetime.datetime.strptime(date, strftime_format)


now = datetime.datetime.now()
print(to_string(now))
