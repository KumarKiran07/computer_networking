import socket
host = "localhost"
port =5555
# sok = socket.socket()also valid instead of following statement
sok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sok.bind((host,port))
print("server start")
sok.listen()
client,addr = sok.accept()
print(client)
print(addr)
print("client address: ", str(addr))
msg = " Hello client how are you?"
client.send(msg.encode())
recMsg = client.recv(1024)
print(recMsg.decode())
#client.send(b'Bye') # another way to encode the message in binary, i.e without using encode()
#client.close()
#print("Bye")
