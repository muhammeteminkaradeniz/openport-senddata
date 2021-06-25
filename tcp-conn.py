import socket

#Mesaj göndermek amacıyla port açtım.
s=socket.socket()

#Alıcı ip port bilgilerini giriyorum
host='192.168.1.105'
port=443

try:
    s.connect((host,port))
    print('{} adresi ile bağlantı kuruldu'.format(host))
    
    yanıt=s.recv(1024)
    print(yanıt.decode('utf-8'))

    s.close()

except socket.error as msg:
    print('[Server aktif değil] Mesaj:',msg)
    