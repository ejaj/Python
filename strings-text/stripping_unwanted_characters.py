import re

s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))
s = ' hello world \n'
print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))
