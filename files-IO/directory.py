import os
import glob
from fnmatch import fnmatch
import sys

# names = os.listdir('/Users/kazi/Projects/pure-python')
# print(names)

# names = [name for name in os.listdir('/Users/kazi/Projects/pure-python')
#          if os.path.isfile(os.path.join('/Users/kazi/Projects/pure-python', name))]
# print(names)

# dirnames = [name for name in os.listdir('/Users/kazi/Projects/pure-python')
#             if os.path.isdir(os.path.join('/Users/kazi/Projects/pure-python', name))]
# print(dirnames)
# pyfiles = [name for name in os.listdir('/Users/kazi/Projects/pure-python')
#            if name.endswith('.py')]
# print(pyfiles)
#
# pyfiles = glob.glob('somedir/*.py')


pyfiles = [name for name in os.listdir('/Users/kazi/Projects/pure-python')
           if fnmatch(name, '*.py')]
print(pyfiles)
print(sys.getfilesystemencoding())


# Printing Bad Filenames
def bad_filename(filename):
    return repr(filename)[1:-1]


filename = "/Users/kazi/Projects/pure-python"
try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))
