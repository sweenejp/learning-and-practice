import datetime

fmt = '%Y%m%d%H%M'
current_time = datetime.datetime.now()
print(current_time.strftime(fmt))