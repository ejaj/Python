import getpass
import os
import subprocess

user = getpass.getuser()
passwd = getpass.getpass()

# Getting the Terminal Size
size = os.get_terminal_size()
print(size)

# Executing an External Command and Getting Its Output
out_bytes = subprocess.check_output(['netstat', '-a'])
out_text = out_bytes.decode('utf-8')
try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output  # Output generated before error
    code = e.returncode  # Return code

# sending it input
# Some text to send
text = b'''
hello world
this is a test
goodbye
'''
# Launch a command with pipes
p = subprocess.Popen(['wc'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
# Send the data and get the output
stdout, stderr = p.communicate(text)
# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
