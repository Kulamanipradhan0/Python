'''
Print the current date and time in specified format
2020/08/01 12:00:00.000
'''

import datetime

now = datetime.datetime.now()

print(str(now.strftime("%Y/%m/%d %H:%M:%S.%f")[:23]))