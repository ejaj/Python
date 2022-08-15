import time
from functools import wraps, partial
from datetime import datetime
import logging
from inspect import signature


# def timethis(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, end - start)
#         return result
#
#     return wrapper
#
#
# @timethis
# def coundown(n):
#     while n > 0:
#         n -= 1
#
#
# # coundown(10000)
#
# # def do_something(func):
# #     @wraps(func)
# #     def wrapper(n, m):
# #         return func(n, m)
# #
# #     return wrapper
# #
# #
# # @do_something
# # def add(n, m):
# #     return n + m
# #
# #
# # print(add(5, 5))
# #
# #
# # def function_logger(f):
# #     def wrapper(*args, **kwargs):
# #         # store the current date and time, and function details
# #         # into a log file:
# #         date_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
# #         with open("log.txt", "a") as logfile:
# #             logfile.write(f'{f.__name__}: {args}, {date_time}\n')
# #         return f(*args, **kwargs)
# #
# #     return wrapper
# #
# #
# # @function_logger
# # def add(n, m):
# #     return n + m
# #
# #
# # @function_logger
# # def square(n):
# #     return n ** 2
# #
# #
# # print(add(4, 5))
# # print(square(2))
# #
# #
# # # with agruments
# # def logger(filename):
# #     def function_logger(f):
# #         def wrapper(*args, **kwargs):
# #             date_time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
# #             with open(filename, "a") as logfile:
# #                 logfile.write(
# #                     f'{f.__name__}: {args}, {date_time}\n')
# #             return f(*args, **kwargs)
# #
# #         return wrapper
# #
# #     return function_logger
# #
# #
# # @logger('log1.txt')
# # def add(n, m):
# #     return n + m
# #
# #
# # @logger('log2.txt')
# # def square(n):
# #     return n ** 2
# #
# #
# # print(add(4, 5))
# # print(square(2))
#
#
# # multiple decorators
# def decor1(func):
#     def wrap():
#         print("doc1")
#         func()
#
#     return wrap
#
#
# def decor2(func):
#     def wrap():
#         print("doc2")
#         func()
#
#     return wrap
#
#
# @decor1
# @decor2
# def say_hello():
#     print("Hello")
#
#
# say_hello()
#
#
# def logged(level, name=None, message=None):
#     def decorate(func):
#         logname = name if name else func.__module__
#         log = logging.getLogger(logname)
#         logmsg = message if message else func.__name_
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             log.log(level, logmsg)
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorate
#
#
# # Example use
# @logged(logging.DEBUG)
# def add(x, y):
#     return x + y
#
#
# @logged(logging.CRITICAL, 'example')
# def spam():
#     print('Spam!')


## Important note: Use a factory decorator to return a decorator that accepts arguments.

## Defining a Decorator with User Adjustable Attributes
# def attach_wrapper(obj, func=None):
#     if func is None:
#         return partial(attach_wrapper, obj)
#     setattr(obj, func.__name__, func)
#     return func
#
#
# def logged(level, name=None, message=None):
#     '''
#     Add logging to a function. level is the logging
#     level, name is the logger name, and message is the
#     log message. If name and message aren't specified,
#     they default to the function's module and name.
#     '''
#
#     def decorate(func):
#         logname = name if name else func.__module__
#         log = logging.getLogger(logname)
#         logmsg = message if message else func.__name__
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             log.log(level, logmsg)
#             return func(*args, **kwargs)
#             # Attach setter functions
#
#         @attach_wrapper(wrapper)
#         def set_level(newlevel):
#             nonlocal level
#
#             level = newlevel
#
#         @attach_wrapper(wrapper)
#         def set_message(newmsg):
#             nonlocal logmsg
#             logmsg = newmsg
#
#         return wrapper
#
#     return decorate
#
#
# # Example use
# @logged(logging.DEBUG)
# def add(x, y):
#     return x + y
#
#
# @logged(logging.CRITICAL, 'example')
# def spam():
#     print('Spam!')

# Defining a Decorator That Takes an Optional Argument
#
# def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
#     if func is None:
#         return partial(logged, level=level, name=name, message=message)
#     logname = name if name else func.__module__
#     log = logging.getLogger(logname)
#     logmsg = message if message else func.__name_
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         log.log(level, logmsg)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# # Example use
# @logged
# def add(x, y):
#     return x + y
#
#
# @logged(level=logging.CRITICAL, name='example')
# def spam():
#     print('Spam!')


# Enforcing Type Checking on a Function Using a Decorator

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):

        # If in optimized mode, disable type checking
        if not __debug__:
            return func
        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):

            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)

        return wrapper

    return decorate


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


spam(1, 2, 3)
spam(1, 'hello', 3)
spam(1, 'hello', 'world')
