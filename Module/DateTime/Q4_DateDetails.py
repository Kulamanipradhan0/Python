'''
Take the below date and print date, month,year,hour,second,minute,weekday,day,UTC time, localtime
Example : 2020-05-13 22:40:41.120
'''

import datetime as dt
print(dir(dt.datetime))
current_date = dt.datetime(2020,05,13,22,40,41,120000)

print('Year',current_date.year)
print('Month',current_date.month)
print('Date',current_date.day)
print('Hour',current_date.hour)
print('Minute',current_date.minute)
print('Second',current_date.second)
print('Milli Second',current_date.microsecond)
print('weekday',current_date.weekday())
print('Day',current_date.strftime('%A'))
print('UTC Time',current_date.strftime('%Z'))