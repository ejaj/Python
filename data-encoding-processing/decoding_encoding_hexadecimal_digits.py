import binascii
import base64
from struct import Struct

s = b'hello'
h = binascii.b2a_hex(s)
print(h)
print(binascii.a2b_hex(h))
b64 = base64.b16decode(s)
print(b64)


# Reading and Writing Binary Arrays of Structures

def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


records = [(1, 2.3, 4.5),
           (6, 7.8, 9.0),
           (12, 13.4, 56.7)]
with open('data.b', 'wb') as f:
    write_records(records, '<idd', f)


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


with open('data.b', 'rb') as f:
    for rec in read_records('<idd', f):
        print(rec)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


with open('data.b', 'rb') as f:
    data = f.read()
    for rec in unpack_records('<idd', data):
        print(rec)
