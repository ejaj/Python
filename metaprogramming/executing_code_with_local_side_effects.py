a = 13
exec('b = a+1')
print(b)


def test():
    a = 13
    loc = locals()
    exec('b = a+1')
    b = loc['b']
    print(b)
