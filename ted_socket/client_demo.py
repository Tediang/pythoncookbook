import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.151',7777))
host,port = sock.getsockname()
print(host, ":", port)


sock.sendall(b'liang xu')
data = sock.recv(1024)
print(data.decode())