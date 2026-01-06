import socket

ports = [22, 80, 22, 443]
local_host_name = socket.gethostbyname('localhost')
ip = socket.gethostbyname(socket.gethostbyname(local_host_name))

for port in ports:
    try:
        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serv.bind((ip,port))
    except:
        print('Port is open',port)
    serv.close