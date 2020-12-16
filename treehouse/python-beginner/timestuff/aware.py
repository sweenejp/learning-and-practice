import datetime

import datetime

pacific = datetime.timezone(datetime.timedelta(hours=-8))

europe = datetime.timezone(datetime.timedelta(hours=+1))

naive = datetime.datetime(2015, 10, 21, 4, 29)

hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)

paris = hill_valley.astimezone(europe)

print(hill_valley.astimezone(pacific).tzinfo)
