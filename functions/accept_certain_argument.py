def recv(max_size, *, block):
    pass


recv(1024, block=False)
recv(1024, block=True)


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


minimum(1, 5, 2, -5, 10)  # Returns -5
minimum(1, 5, 2, -5, 10, clip=0)  # Returns


# Attaching Informational Metadata to Function Arguments

def add(x: int, y: int) -> int:
    return x + y


print(help(add))


# Returning Multiple Values from a Function

def myfun():
    return 1, 2, 3


a, b, c = myfun()
print(a)
print(b)
print(c)


# Defining Functions with Default Arguments
def spam(a, b=42):
    print(a, b)


spam(1)  # Ok. a=1, b=42
spam(1, 2)  # Ok. a=1, b=2
