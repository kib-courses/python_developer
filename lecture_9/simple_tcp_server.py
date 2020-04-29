import os
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 7777)
print('PID=%d, running at %s:%s' % (os.getpid(), *server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    # blocking call
    connection, client_address = sock.accept()
    print('Incoming transmission: ', client_address)
    data: bytes = b""
    while True:
        # blocking call
        data_i: bytes = connection.recv(8)
        if len(data_i) == 0:
            # Skipping empty sendings - form slow clients
            continue
        print(' ~~~ received batch "%s"' % data_i)
        data += data_i
        if data.count(b'"') == 2:
            break
        else:
            continue
    data_repr = data.decode()
    sending = data_repr[::-1]
    connection.sendall(sending.encode())
    print('Got its kicks (%s), %s' % (client_address, sending))
    connection.close()