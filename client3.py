import socket
host = "192.168.0.1"
port = 80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
buf = b'-' * 30
s.send(b'GET /HTTP/1.1\r\n\r\n')
resp = s.recv(2048)
print("Number of bytes",len(resp))
print(buf.decode())
s.close()
