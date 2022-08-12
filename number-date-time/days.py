from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
from datetime import datetime, date, timedelta
import calendar

# a = timedelta(days=2, hours=6)
# b = timedelta(hours=4.5)
# c = a + b
# print(c.days)
# print(c.seconds)
# print(c.total_seconds()/3600)

# a = datetime(2012, 9, 23)
# print(a + timedelta(days=10))
# b = datetime(2012, 12, 21)
# d = b - a
# print(d.days)
# now = datetime.today()
# print(now)
# print(now + timedelta(minutes=10))
# a = datetime(2012, 9, 23)
# print(a + relativedelta(months=+1))
# print(a + relativedelta(months=+4))


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_date_time_by_day(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


# The optional start_date can be supplied using another datetime instance.

# print(datetime.today())
# print(get_date_time_by_day('Tuesday'))
# print(get_date_time_by_day('Sunday', datetime(2012, 12, 21)))

# Next Frida
# d = datetime.now()
# print(d + relativedelta(weekday=FR))
# Last Frida
# print(d + relativedelta(weekday=FR(-1)))

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


a_day = timedelta(days=1)
first_day, last_day = get_month_range()

while first_day < last_day:
    print(first_day)
    first_day += a_day


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1), timedelta(hours=6)):
    print(d)
