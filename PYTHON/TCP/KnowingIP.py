import socket
host = "localhost"
try:
    addr = socket.gethostbyname(host)
    print('ip address', addr)
except:
    print("local host not valid")
