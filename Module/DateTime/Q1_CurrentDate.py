'''
Print today(Only date with specified format
21st January 2020
'''

import datetime

today = datetime.date.today()

print(today.strftime('%d %B %Y'))
