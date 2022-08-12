from queue import Queue
from functools import wraps
import sys


# def apply_async(func, args, *, callback):
#     # Compute the result
#     result = func(*args)
#     # Invoke the callback with the result
#     callback(result)
#
#
# def print_result(result):
#     print("Got", result)
#
#
# def add(x, y):
#     return x + y
#
#
# apply_async(
#     add,
#     (2, 3),
#     callback=print_result
# )
# apply_async(
#     add,
#     ('hello', 'world'),
#     callback=print_result()
# )
#
#
# # carry extra information
# class ResultHandler:
#     def __init__(self):
#         self.sequence = 0
#
#     def handler(self, result):
#         self.sequence += 1
#         print('[{}] Got: {}'.format(self.sequence, result))
#
#
# r = ResultHandler()
# apply_async(
#     add,
#     (2, 3),
#     callback=r.handler
# )
#
#
# def make_handler():
#     sequence = 0
#
#     def handler(result):
#         nonlocal sequence
#         sequence += 1
#         print('[{}] Got: {}'.format(sequence, result))
#
#     return handler
#
#
# handler = make_handler()
# apply_async(
#     add,
#     (2, 3),
#     callback=handler
# )

# def sample():
#     n = 0
#
#     def func():
#         print('n=', n)
#
#     def get_n():
#         return n
#
#     def set_n(val):
#         nonlocal n
#         n = val
#
#     func.get_n = get_n
#     func.set_n = set_n
#     return func
#
#
# f = sample()
# print(f())

class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
print(s)
