from socketserver import BaseRequestHandler, UDPServer, ThreadingUDPServer
import time
from socket import socket, AF_INET, SOCK_DGRAM


class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


serv = UDPServer(('', 20000), TimeHandler)
# concurrent operation
# serv = ThreadingUDPServer(('',20000), TimeHandler
serv.serve_forever()

# To test the server, run it and then open a separate Python process that sends messages to it
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'', ('localhost', 20000))
s.recvfrom(8192)


def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)


time_server(('', 20000))
