import textwrap
import os

# parts = ['Is', 'Chicago', 'Not', 'Chicago?']
# print(' '.join(parts))
# print(', '.join(parts))
# print(''.join(parts))
#
# a = "Kazi"
# b = "Ejajul"
# c = "Madaripur"
# print(a + ' ' + b)
# print('{} {}'.format(a, b))
# data = ['ACME', 50, 91.1]
# print(','.join(str(d) for d in data))
# print(a + ':' + b + ':' + c)  # Ugly
# print(':'.join([a, b, c]))  # Still Ugly
# print(a, b, c, sep=':')  # better
#
#
# def sample():
#     yield 'Is'
#     yield 'Chicago'
#     yield 'Not'
#     yield 'Chicago?'
#
#
# text = ''.join(sample())
#
#
# def combine(source, maxsize):
#     parts = []
#     size = 0
#     for part in source:
#         parts.append(part)
#     size += len(part)
#     if size > maxsize:
#         yield ''.join(parts)
#     parts = []
#     size = 0
#     yield ''.join(parts)
#
#
# for part in combine(sample(), 32768):
#     pass
#     # f.write(part)

# Interpolating Variables in Strings
# s = '{name} has {n} messages.'
# print(s.format(name='Ejaj', m=37))

# name = 'Guido'
# n = 37
# print(s.format_map(vars()))


# class Info:
#     def __init__(self, name, n):
#         self.name = name
#         self.n = n
#
#
# a = Info('Ray', 28)
# s.format_map(vars(a))

# handle missing values.
# class SafeSub(dict):
#     def __missing__(self, key):
#         return '{' + key + '}'
#
#
# del n
# s.format_map(SafeSub(vars()))

# Reformatting Text to a Fixed Number of Column
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent=' '))
print(textwrap.fill(s, 40, subsequent_indent=' '))
# print(os.get_terminal_size().columns)
