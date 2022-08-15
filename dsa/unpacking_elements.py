from statistics import mean


def drop_first_last(grades):
    first, *middle, last = grades
    return mean(middle)


# user_record = ('Devops', 'devops@gmail.com', '01709087', '01769087')
# name, email, *phone_numbers = user_record
# print(name)
# print(phone_numbers)
# *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
# print(trailing)
# print(current)


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


# for tag, *arg in records:
#     if tag == 'foo':
#         do_foo(*arg)
#     elif tag == 'bar':
#         do_bar(*arg)

# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname)
# print(*fields)
# print(homedir)
# print(sh)

# record = ('ACME', 50, 123.45, (12, 18, 2012))
# name, *_, (*_, year) = record
# print(name)
# print(year)

# items = [1, 10, 7, 4, 5, 9]
# head, *tail = items
# print(head)
# print(tail)

def sum(itmes):
    head, *tail = itmes
    return head + sum(tail) if tail else head


items = [1, 10, 7, 4, 5, 9]
print(sum(items))
