"""Trying out ome (server side) socket code taken from here:
https://stackoverflow.com/questions/16130786/why-am-i-getting-the-error-connection-refused-in-python-sockets"""

import socket

s = socket.socket()
port = 12397
s.bind(('',port))

s.listen(5)
while True:
    c, addr = s.accept()
    print "Got connection from", addr
    c.send("Thank you for connecting!")
    c.close()
