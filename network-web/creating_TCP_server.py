from socketserver import BaseRequestHandler, StreamRequestHandler, ThreadingTCPServer, TCPServer
import socket
from socket import socket, AF_INET, SOCK_STREAM


# class EchoHandler(BaseRequestHandler):
#     # Optional settings (defaults shown)
#     timeout = 5  # Timeout on all socket operations
#     rbufsize = -1  # Read buffer size
#     wbufsize = 0  # Write buffer size
#     disable_nagle_algorithm = False  # Sets TCP_NODELAY socket option
#
#     def handle(self):
#         print('Got connection from', self.client_address)
#         # while True:
#         #     msg = self.request.recv(8192)
#         #     if not msg:
#         #         break
#         #     self.request.send(msg)
#         try:
#             for line in self.rfile:
#             # self.wfile is a file-like object for writing
#                 self.wfile.write(line)
#         except socket.timeout:
#             print('Timed out!')

# serv = TCPServer(('', 20000), EchoHandler)
# handle multiple clients,
# serv = ThreadingTCPServer(('', 20000), EchoHandler)
# Set up various socket options
# serv.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
# # Bind and activate
# serv.server_bind()
# serv.server_activate()
# serv.serve_forever()
# serv.serve_forever()

# class EchoHandler(StreamRequestHandler):
#     def handle(self):
#         print('Got connection from', self.client_address)
#         # self.rfile is a file-like object for reading
#         for line in self.rfile:
#         # self.wfile is a file-like object for writing
#             self.wfile.write(line)

# To test the server, run it and then open a separate Python process that connects to it:
# from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
#
# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('localhost', 20000))
# s.send(b'Hello')
# s.recv(8192)


def echo_handler(address, client_sock):
    print('Got connection from {}'.format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()


def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)


echo_server(('', 20000))
