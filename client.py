import socket


sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(b'hello')

data = sock.recv(1024)
sock.close()

print(data)