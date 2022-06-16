import re

str = 'My roll number is 489'

res = re.findall('\d',str)
print(res)
