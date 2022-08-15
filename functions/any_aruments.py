import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


print(avg(1, 2))
print(avg(1, 2, 3, 4))


# any number of keyword arguments,

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))

    return element


el = make_element('item', 'Albatross', size='large', quantity=6)
print(el)
print(make_element('p', '<spam>'))


def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict
