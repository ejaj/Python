import weakref


class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstance):
    @staticmethod
    def foo(x):
        print("Spam.foo")


Spam.foo(42)
s = Spam()  # Got error


# singleton pattern
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class ABC(metaclass=Singleton):
    def __init__(self):
        print("Creating Spam")


a = Spam()
b = Spam()
print(a is b)  # True
c = Spam()
print(a is c)  # True


# cached instances

class Cached(type):
    def __init__(self, *args, **kwargs):
        super(Cached, self).__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name
