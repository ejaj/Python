import re
import unicodedata
from calendar import month_abbr

# text = 'yeah, but no, but yeah, but no, but yeah'
# replace_text = text.replace('yeah', 'yep')
# print(replace_text)

# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# datepat.sub(r'\3-\1-\2', text)
#
#
# def change_date(m):
#     mon_name = month_abbr[int(m.group(1))]
#     return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
#
#
# datepat.sub(change_date, text)

# Case-Insensitive Text
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

# unicodedata
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
if t1 == t2:
    print(True)
else:
    print(False)
