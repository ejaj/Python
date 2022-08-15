import shutil
import os.path

src = 'sample.text'
dst = ''
shutil.copy(src, dst)
# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)
# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)
# Move src to dst (mv src dst)
shutil.move(src, dst)

# supply the follow_symlinks keyword argument like this:
shutil.copy2(src, dst, follow_symlinks=False)
# preserve symbolic links
shutil.copytree(src, dst, symlinks=True)

# def ignore_pyc_files(dirname, filenames):
#     return [name in filenames if name.endswith('.pyc')]


# shutil.copytree(src, dst, ignore=ignore_pyc_files)

filename = '/Users/guido/programs/spam.py'
os.path.basename(filename)

# Creating and Unpacking Archives
shutil.unpack_archive('Python-3.3.0.tgz')
shutil.make_archive('py33', 'zip', 'Python-3.3.0')
shutil.get_archive_formats()
