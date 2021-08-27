'''
Load a json content to python
'''

import json

item = '{"fruit": "Apple","size": "Large","color": "Red"}'

print(dir(json))

y = json.loads(item)
for i in y.keys():
    print(i)