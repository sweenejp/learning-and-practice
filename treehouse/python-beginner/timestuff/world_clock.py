from datetime import datetime
import pytz

other_timezones = [('Minneapolis', 'US/Central'),
                   ('Mumbai', 'Asia/Calcutta'),
                   ('London', 'Europe/London'),
                   ('Tokyo', 'Asia/Tokyo'),
                   ('San Francisco', 'US/Pacific'),
                   ('New York', 'US/Eastern'),
                   ('Varena', 'Europe/Rome')]


def world_clock():
    fmt = '%m/%d %I:%M %p'
    local_time = datetime.now()
    local_time = pytz.timezone('US/Central').localize(local_time)
    local_time_utc = local_time.astimezone(pytz.utc)

    for timezone in other_timezones:
        time = local_time_utc.astimezone(pytz.timezone(timezone[1]))
        print('The time in {} is {}'.format(timezone[0], time.strftime(fmt)))


world_clock()

