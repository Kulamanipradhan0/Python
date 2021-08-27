import datetime

print (dir(datetime))

print(datetime.MAXYEAR,datetime.MINYEAR)

print (dir(datetime.date))

a = datetime.date
today = a.today()
print(today.strftime('%d %B %Y'))

print(a.weekday(today))


x = datetime.datetime(2020,05,21)
print(x.strftime('%d %B %y %H %M %S'))

