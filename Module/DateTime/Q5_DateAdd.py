'''
Add two dates together
Add intervals to a date
'''
import datetime as dt

today = dt.datetime.today()
print (today)
print(today+dt.timedelta(days=5))


print(today+dt.timedelta(days=5,hours=10))


#Add two existing dates together

date1 = dt.datetime(2020,05,13)
date2 = dt.datetime(2020,05,12)

dob = dt.date(1992,06,12)
today = dt.date.today()
age = today - dob
print(age.days/365)
#print(year)

