import os
import socket
from click import prompt

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = ('localhost', 7777)
print('PID=%d, connecting to %s port %s' % (os.getpid(), *server_address))
sock.connect(server_address)

while True:
        message = ('"'+prompt("Enter message, to stop - STOP/Ctrl-C", type=str)+'"').encode()
        if message == 'STOP':
            break
        sock.sendall(message)
        receiver = b""
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            # блокирующий вызов
            data = sock.recv(8)
            receiver += data
            amount_received += len(data)
            print(' ~~~ received %s' % data)
        print("Final answer: %s" % receiver.decode())

sock.close()
