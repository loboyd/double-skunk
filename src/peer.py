"""This module will implement the basic peer to peer functionality using the
built-in socket library."""

import socket #import socket module
import time
import random


def exchange(addr, send_data):
    """Exchange two pieces of data with socket connections. This function
    assumes both peers call it at approximately the same time. Otherwise,
    it will hang (should probably implement a timeout in the future)."""

    host = addr[0]
    port = addr[1]

    sent = 0
    received = 0

    while not (sent and received):
        # try being the client
        if not received:
            s = socket.socket()
            s.settimeout(0.1)

            try:
                s.connect(addr)
                recv_data = s.recv(1024)
                received = 1
            except:
                pass

            s.close()

        # try being the server
        if not sent:
            s = socket.socket()
            s.bind(('', port))
            s.listen(5)
            c, _ = s.accept()
            c.send(send_data)
            c.close()
            sent = 1

    return recv_data

def get_peer_ip():
    """Get IP address of a friend. (DO SOME SANITY CHECKING HERE.)
    Eventually, nodes should publish their IP's to a server along with unique keys so that
    peer nodes can just query the server. For true peer-to-peer, some type of routing would
    need to be implemented."""
    return raw_input("Please input your friend's public IP address:\n")
