from datetime import datetime
from pytz import timezone

# text = '2012-09-20'
# y = datetime.strptime(text, '%Y-%m-%d')
# z = datetime.now()
# diff = z - y
# print(diff)

d = datetime(2012, 12, 21, 9, 30, 0)
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
bang_d = loc_d.astimezone(timezone('Asia/Dhaka'))
print(bang_d)