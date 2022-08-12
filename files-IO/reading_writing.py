import array
import os
import gzip
import bz2
from functools import partial
import os
import mmap

with open('hello.txt', 'rt') as f:
    data = f.read()

with open('hello.txt', 'rt') as f:
    for line in f:
        print(line)


# with open('somefile.bin', 'rb') as f:
#     data = f.read(16)
#     text = data.decode('utf-8')
# with open('somefile.bin', 'wb') as f:
#     text = 'Hello World'
#     f.write(text.encode('utf-8'))

# nums = array.array('i', [1, 2, 3, 4])
# with open('data.bin', 'wb') as f:
#     f.write(nums)

# if not os.path.exists('extra'):
#     with open('extra', 'wt') as f:
#         f.write('Hello\n')
# else:
#     print("File Already Exist")

# gzip compression

# with gzip.open('somefile.gz', 'rt') as f:
#     text = f.read()
#
# # bz2 compression
# with bz2.open('somefile.bz2', 'rt') as f:
#     text = f.read()

# RECORD_SIZE = 32
# with open('somefile.data', 'rb') as f:
#     records = iter(partial(f.read, RECORD_SIZE), b'')
#     for r in records:
#         pass

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)
