from itertools import zip_longest, chain
from collections import Iterable
import heapq

# my_list = ['a', 'b', 'c']
# for idx, val in enumerate(my_list):
#     print(idx, val)
# for idx, val in enumerate(my_list, 1):
#     print(idx, val)
#
# data = [(1, 2), (3, 4), (5, 6), (7, 8)]
# for n, (x, y) in enumerate(data):
#     print(n)
#     print(x)
#     print(y)

# Iterating Over Multiple Sequences Simultaneously
# xpts = [1, 5, 4, 2, 10, 7]
# ypts = [101, 78, 37, 15, 62, 99]
# for x, y in zip(xpts, ypts):
#     print(x, y)

#

# for i in zip_longest(a, b):
#     print(i)
# for i in zip_longest(a, b, fillvalue=0):
#     print(i)

# headers = ['name', 'shares', 'price']
# values = ['ACME', 100, 490.1]
# s = dict(zip(headers, values))
# print(s)
# for name, val in zip(headers, values):
#     print(name, '=', val)

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)


# Flattening a Nested Sequence

def flatten(itmes, ignore_types=(str, bytes)):
    for x in itmes:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

a = [1, 2, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
