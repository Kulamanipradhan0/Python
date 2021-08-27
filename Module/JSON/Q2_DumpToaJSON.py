'''
Create a json file from a python dictionary
'''
import  json
book = {'Name':'Unix Shell Programming','Writer':'Yashavant Kanetkan','Published By':'BPB Publication','Id':'ISBN 81-7029-753-2'}

book_json = json.dumps(book,indent=2,separators=(',',':'),sort_keys=True)
print(book_json)