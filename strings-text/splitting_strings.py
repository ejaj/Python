import re
from fnmatch import fnmatch, fnmatchcase

line = 'asdf fjdk; afed, fjek,asdf, foo'
l = re.split(r'[;,\s]\s*', line)
# print(l)
fields = re.split(r'(;|,|\s)\s*', line)
# print(fields)
# values = fields[::2]
# delimiters = fields[1::2] + ['']
# print(values)
# print(delimiters)
# print(''.join(v + d for v, d in zip(values, delimiters)))

# starts & end with
# choices = ['http:', 'ftp:']
# url = 'http://www.python.org'
# print(url.startswith(tuple(choices)))

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

# On OS X (Mac)
print(fnmatch('foo.txt', '*.TXT'))
# On Windows
print(fnmatch('foo.txt', '*.TXT'))

# distinction matters
print(fnmatchcase('foo.txt', '*.TXT'))

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print("yes")
else:
    print("no")
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

