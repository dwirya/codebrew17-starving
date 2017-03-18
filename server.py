# from socket import *
# from threading import Thread



# def clientHandler(socket): 
# 	conn, addr = s.accept() 
# 	print (addr)#, (" is Connected" )
# 	while 1: 
# 		data = conn.recv(1024) 
# 		if not data:
# 			break 
# 		print ("Received Message"), repr(data.decode("utf-8"))

# HOST = '' #localhost
# https://www.youtube.com/watch?v=4mPd-xgD0NQ
# PORT = 8000

# s = socket(AF_INET, SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(3)
# print ("Server is running......")

# for i in range(3):
# 	Thread(target=clientHandler(s)).start()

# s.close()


# import socket
from socket import *
# from socket import socket, bind, listen, recv, send 

HOST = '' #localhost / 192.168.1.1
# LAN - 192.168.1.1
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)# 98% of all socket programming will use AF_INET and SOCK_STREAM
s.bind((HOST, PORT)) 
s.listen(1) # how many connections it can receive at one time 
conn, addr = s.accept() # accept the connection
print ('Connected by' +str(addr)) # print the address of the person connected
while True: 
	data = conn.recv(1024) #receives datae (1024 bytes) using conn and store into data 
	print ("Received "+ str(data.decode("utf-8")))#print data; Data is the message the users types 
	reply = input("Reply: ")
	conn.sendall(str.encode(reply))

conn.close()