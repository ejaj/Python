import types
from functools import wraps
import time


#
# class Profiled:
#     def __init__(self, func):
#         wraps(func)(self)
#         self.ncalls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.ncalls += 1
#         return self.__wrapped__(*args, **kwargs)
#
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             return types.MethodType(self, instance)
#
#
# @Profiled
# def add(x, y):
#     return x + y
#
#
# class Spam:
#     @Profiled
#     def bar(self, x):
#         print(self, x)

# Applying Decorators to Class and Static Method

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r

    return wrapper


class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


s = Spam()
s.instance_method(1000000)
