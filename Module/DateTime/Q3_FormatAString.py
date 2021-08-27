'''
Take the below date and convert it into specified formt below
Example : 2020-01-01 12:12:12
Output : 1 Jan 20 12:12:12.000
'''

import datetime as dt

current_date = dt.datetime(2020,01,01,12,12,12)
print (current_date.strftime("%d %b %y %H:%M:%S.000"))


