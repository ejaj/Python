import logging
from functools import partial
import math
from multiprocessing import Pool
from urllib.request import urlopen


# add = lambda x, y: x + y
# print(add(2, 3))
# names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
# print(sorted(names, key=lambda name: name.split()[-1].lower()))
#
#
# # reduce the number of arguments
# def spam(a, b, c, d):
#     print(a, b, c, d)
#
#
# s1 = partial(spam, 1)
# s1(2, 3, 4)
#
# points = [(1, 2), (3, 4), (5, 6), (7, 8)]
#
#
# def distance(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return math.hypot(x2 - x1, y2 - y1)
#
#
# pt = (4, 3)
# points.sort(key=partial(distance, pt))
# print(points)
#
#
# def output_result(result, log=None):
#     if log is not None:
#         log.debug('Got: %r', result)
#
#
# # A sample function
# def add(x, y):
#     return x + y
#
#
# logging.basicConfig(level=logging.DEBUG)
# log = logging.getLogger('test')
# p = Pool()
# p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
# p.close()
# p.join()


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
