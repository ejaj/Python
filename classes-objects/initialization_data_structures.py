import math


# class Structure:
#     _fields = []
#
#     def __init__(self, *args):
#         if len(args) != len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#
#
# class Stock(Structure):
#     _fields = ['name', 'shares', 'price']
#
#
# class Point(Structure):
#     _fields = ['x', 'y']
#
#
# class Circle(Structure):
#     _fields = ['radius']
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#
# s = Stock('ACME', 50, 91.1)
# p = Point(2, 3)
# c = Circle(4.5)
# s2 = Stock('ACME', 50)

# support keyword arguments

class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        for name in self._fields[len(args)]:
            setattr(self, name, kwargs.pop(name))
        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


s2 = Stock('ACME', 50, price=91.1)
s3 = Stock('ACME', shares=50, price=91.1)
s1 = Stock('ACME', 50, 91.1)
