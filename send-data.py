import socket

HOST = '192.168.1.105'
PORT = 443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'hello,world')
    data =s.recv(1024)

print('Recived',repr(data))

    
