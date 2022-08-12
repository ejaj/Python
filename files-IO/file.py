import threading
import time
import urllib.request
import io
import sys
from socket import socket, AF_INET, SOCK_STREAM
from tempfile import TemporaryFile
import serial
import pickle


# u = urllib.request.urlopen('http://www.python.org')
# f = io.TextIOWrapper(u, encoding='utf-8')
# text = f.read()
# print(text)
# print(sys.stdout.encoding)

# Writing Bytes to a Text Fil
# sys.stdout.write(b'Hello\n')

# def echo_client(client_sock, addr):
#     print('Got connection from', addr)
#     client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
#                      closefd=False)
#     client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
#                       closefd=False)
#     for line in client_in:
#         client_out.write(line)
#         client_out.flush()
#     client_sock.close()
#
#
# def echo_server(address):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(address)
#     sock.listen(1)
#     while True:
#         client, addr = sock.accept()
#         echo_client(client, addr)
#
#
# with TemporaryFile('w+t') as f:
#     # Read/write to the file
#     f.write('Hello World\n')
#     f.write('Testing\n')
#     # Seek back to beginning and read the data
#     f.seek(0)
#     data = f.read()

# Communicating with Serial Ports

# ser = serial.Serial(
#     '/dev/tty.usbmodem641',  # Device name
#     baudrate=9600,
#     bytesize=8,
#     parity='N',
#     stopbits=1
# )

# Serializing Python Objects

# data = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(pickle.dump(data))

class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


countdown = Countdown(10)
print(countdown)
