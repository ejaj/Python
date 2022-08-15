s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)


def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s


# Aligning Text Strings
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.rjust(20, '='))
print(text.center(20, '*'))
print(text.center(20, '*'))
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>20s'))
print(format(text, '*^20s'))
