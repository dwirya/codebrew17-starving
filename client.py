from socket import *

HOST = ''
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # client-side, connects to a host
while True: 
	message = input("Your Message: ") 
	s.send(str.encode(message))
	print ("Awaiting reply")
	reply = s.recv(1024) # 1024 is max data that can be received 
	print ("Received " + reply.decode("utf-8"))

s.close()