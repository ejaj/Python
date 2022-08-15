# class A:
#     def spam(self, x):
#         pass
#
#     def foo(self):
#         pass
#
#
# class B:
#     def __init__(self):
#         self._a = A()
#
#     def __getattr__(self, item):
#         return getattr(self._a, item)
#
#
# b = B()
# b.bar()  # Calls B.bar() (exists on B)
# b.spam(42)  # Calls B.__getattr__('spam') and delegates to A.spam

# Another way
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        print('getattr', item)
        return getattr(self._obj, item)

    def __setitem__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('delattr:', item)
            delattr(self._obj, item)


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


# Create an instance
s = Spam(2)
# Create a proxy around it
p = Proxy(s)
# Access the proxy
print(p.x)  # Outputs 2
p.bar(3)  # Outputs "Spam.bar: 2 3"
p.x = 37  # Changes s.x to 37
