from urllib.request import urlopen
from pprint import pprint
from collections import OrderedDict

import json

# data = {
#     'name': 'ACME',
#     'shares': 100,
#     'price': 542.23
# }
# json_str = json.dumps(data)
#
# print(json_str)
# data = json.loads(json_str)
# print(data)
# # Writing JSON data
# with open('data.json', 'w') as f:
#     json.dump(data, f)
# # Reading data back
# with open('data.json', 'r') as f:
#     data = json.load(f)
# u = urlopen('https://api.github.com/users/hadley/orgs')
# resp = json.loads(u.read().decode('utf-8'))
#
# pprint(resp)

# OrderedDict
s = '{"name": "ACME", "shares": 50, "price": 490.1}'


# data = json.loads(s, object_pairs_hook=OrderedDict)
# print(data)

class JsonObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JsonObject)
print(data.name)
print(data.shares)
print(data.price)
