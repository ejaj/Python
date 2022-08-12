from collections import ChainMap

# a = {'x': 1, 'z': 3}
# b = {'y': 2, 'z': 4}
# c = ChainMap(a, b)
# print(c['x'])
# print(c['y'])
# print(c['z'])
# values = ChainMap()
# values['x'] = 1
# values = values.new_child()
# values['x'] = 2
# values = values.new_child()
# values['x'] = 3
# print(values)
# print(values['x'])
# print(values.parents)
# print(values['x'])
# print(values.parents)
# print(values['x'])

# alternative of chainMAP
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
