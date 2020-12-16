import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)


def time_machine(num, interval):
    if interval == "minutes":
        return datetime.timedelta(minutes=num) + starter
    if interval == "hours":
        return datetime.timedelta(hours=num) + starter
    if interval == "days":
        return datetime.timedelta(days=num) + starter
    if interval == "years":
        return datetime.timedelta(days=(num*365)) + starter


print(starter)
print(time_machine(10, "days"))
