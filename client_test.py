# """ 192.168.1.149 """
# bradley_ip = '192.168.1.149'
#
# from socket import *
# HOST = bradley_ip
# PORT = 9495
# BUFSIZE = 1024
# ADDR = (HOST, PORT)
# tcpTimeClientSock = socket(AF_INET, SOCK_STREAM)
# tcpTimeClientSock.connect(ADDR)
# while True:
#   data = raw_input('> ')
#   if not data:
#       break
#   tcpTimeClientSock.send(data)
#   data = tcpTimeClientSock.recv(BUFSIZE)
#   if not data:
#       break
# print data
# tcpTimeClientSock.close()


import socket #import socket module

s = socket.socket() #create a socket object
host = '192.168.1.149' #Host i.p
port = 12397 #Reserve a port for your service

s.connect((host,port))
print s.recv(1024)
s.close