"""Trying out some (client end) socket code taken from here:
https://stackoverflow.com/questions/16130786/why-am-i-getting-the-error-connection-refused-in-python-sockets"""

import socket #import socket module

s = socket.socket() #create a socket object
host = '192.168.1.149' #Host i.p
port = 12397 #Reserve a port for your service

s.connect((host,port))
print s.recv(1024)
s.close