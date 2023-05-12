import socket
host='localhost'
port = 5555
sok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sok.connect((host,port))
msg = sok.recv(1024) #1024 size of buffer
print(msg.decode())

msg1 = "I am Fine"
sok.send(msg1.encode())
sok.close()
