class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


# try:
#     msg = s.recv()
# except TimeoutError as e:
# except ProtocolError as e:


# import traceback
# import sys
#
# try:
#     func(arg)
# except:
#     print('**** AN ERROR OCCURRED ****')
#     traceback.print_exc(file=sys.stderr)
