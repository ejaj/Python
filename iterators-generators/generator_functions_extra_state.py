from collections import deque
from itertools import permutations, combinations, combinations_with_replacement


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


# with open('somefile.txt') as f:
#     lines = linehistory(f)
#     for line in lines:
#         if 'python' in line:
#             for lineno, hline in lines.history:
#                 print('{}:{}'.format(lineno, hline), end='')

items = ['a', 'b', 'c']
# for p in permutations(items):
#     print(p)
# for p in permutations(items, 2):
#     print(p)

# combinations
for c in combinations(items, 3):
    print(c)
for c in combinations(items, 2):
    print(c)
for c in combinations(items, 1):
    print(c)
for c in combinations_with_replacement(items, 3):
    print(c)
