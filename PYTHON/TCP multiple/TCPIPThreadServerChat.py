from time import *
from threading import *
from socket import *
class ThreadServer:
	def __init__(self,client,addr):
		self.client=client
		self.addr = addr
	def start(self):
		while(True):
			msg = self.client.recv(1024)
			print('Client Message :(',self.addr,')', msg.decode())
			reply= input('Type reply : ')
			self.client.send(reply.encode())
host = "localhost"
port =5555

sok =socket()
sok.bind((host,port))
sok.listen(5)
print("server start")
while True:
	client,addr = sok.accept()
	print(' Request accept from client address ', str(addr))
	ser = ThreadServer(client,addr)
	thred= Thread(target=ser.start)
	thred.start()
	
client.close()
print("Bye")
