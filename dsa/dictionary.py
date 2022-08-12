from collections import defaultdict, OrderedDict
import json

# d = {
#     'a': [1, 2, 3],
#     'b': [4, 5]
# }
# e = {
#     'a': {1, 2, 3},
#     'b': {4, 5}
# }

# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(3)
# print(d)

# A regular dictionary
# d = {}
# d.setdefault('a', []).append(1)
# d.setdefault('a', []).append(2)
# d.setdefault('b', []).append(4)


# Ordered Dict
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['spam'] = 3
# d['grok'] = 4
# for key in d:
#     print(key, d[key])
# print(json.dumps(d))

# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }

# min_price = min(zip(prices.values(), prices.keys()))
# max_price = max(zip(prices.values(), prices.keys()))
# print(min_price)
# print(max_price)
#
# price_sorted = sorted(zip(prices.values(), prices.keys()))
# print(price_sorted)
# print(min(prices))
# print(max(prices))

# print(min(prices.values()))
# print(max(prices.values()))

# print(min(prices, key=lambda k: prices[k]))
# print(max(prices, key=lambda k: prices[k]))
# min_value = prices[min(prices, key=lambda k: prices[k])
# print(min_value)

# Finding Commonalities
# a = {
#     'x': 1,
#     'y': 2,
#     'z': 3
# }
# b = {
#     'w': 10,
#     'x': 11,
#     'y': 2
# }
#
# print(a.keys() & b.keys())
# print(a.keys() - b.keys())
# print(a.items() & b.items())
# c = {key: a[key] for key in a.keys() - {'z', 'w'}}


# Extracting a Subset of a Dictionary
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# p1 = {key: val for key, val in prices.items() if val > 200}
# print(p1)
# tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
# p2 = {key: value for key, value in prices.items() if key in tech_names}
# print(p2)

#  tuples and passing them to the dict() function
p1 = dict((key, value) for key, value in prices.items() if value > 200)
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: prices[key] for key in prices.keys() & tech_names}
