import datetime
# date_time = time.strftime('%m%d%Y%H%M')

current_day = datetime.datetime.now()

print(type(current_day))
print(current_day)
#date_split = current_day.split(' ')
#print(date_split)

print(current_day.strftime('%m%d%Y%H%M'))
print(current_day.strftime('%Y/%d/%m-%H:%M'))
date_str = current_day.strftime('%Y/%d/%m-%H:%M')
print(type(date_str))
print(date_str)