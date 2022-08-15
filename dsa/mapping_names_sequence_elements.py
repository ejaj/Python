from collections import namedtuple

subscribe = namedtuple('subscribe', ['addr', 'joined'])
sub = subscribe('jonesy@example.com', '2012-10-19')
# sub = subscribe(addr='jonesy@example.com', joined='2012-10-19')
# print(sub)
# print(sub.addr)
# print(sub.joined)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

stock = namedtuple('stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = stock(*rec)
        total += s.shares * s.price
    return total
