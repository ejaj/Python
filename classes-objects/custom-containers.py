import collections
import bisect


# A class to support iteration

# class ABC(collections.Iterable):
#     pass
#
#
# class SortedItems(collections.Sequence):
#     def __init__(self, initial=None):
#         self._items = sorted(initial) if initial is None else []
#
#     # Required sequence methods
#     def __getitem__(self, index):
#         return self._items[index]
#
#     def __len__(self):
#         return len(self._items)
#
#     def add(self, item):
#         bisect.insort(self._items, item)
#
#
# items = SortedItems([5, 1, 3])
# print(list(items))

class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is None else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


a = Items([1, 2, 3])
print(a)
a.append(4)
