"""--------------------------------------------------------------------------"""
"""This code will eventually serve to exchange the players' ``cuts`` of the deck
for determining the first dealer. This can also be easily generalized to any
two-way exchange of two strings."""


import socket #import socket module
import time
import random

host = '192.168.1.100'
port = 12397 #Reserve a port for your service

slf = str(random.random())

sent = 0
received = 0

t1 = time.time()

while not (sent and received):
#while time.time() < t1 + 10:
    # try being the client
    if not received:
        try:
            s = socket.socket()
            s.settimeout(0.1)
            s.connect((host, port))
            opp = s.recv(1024)
            received = 1
            s.close()
        except:
            pass

    # try being the server
    if not sent:
        try:
            s = socket.socket()
            #s.settimeout(0.1)
            s.bind(('', port))
            s.listen(5)
            c, addr = s.accept()
            c.send(slf)
            c.close()
            #s.shutdown(socket.SHUT_RD)
            sent = 1
        except:
            print "attempting to send"
            pass

print "opponent's draw: {0}".format(opp)
print "your draw: {0}".format(slf)
print "you are {0}the dealer.".format('' if float(opp) < float(slf) else 'not ')
s.close
#s.shutdown()
print type(opp)
