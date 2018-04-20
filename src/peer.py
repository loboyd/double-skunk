"""This module will implement the basic peer to peer functionality using the
built-in socket library."""

import socket #import socket module
import time
import random

def send(addr, send_data):
    """Send a piece of data to a peer. The function assumes the other peer
    is listening. THIS WILL HANG IF DATA IS NOT SENT SUCCESSFULLY; TIMEOUT
    SHOULD BE IMPLEMENTED AT SOME POINT"""
    host = addr[0]
    port = addr[1]

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen(5)
    c, _ = s.accept()
    c.send(send_data)
    c.close()

def recv(addr):
    """Receive a piece of data from a peer. The function assumes the other
    peer is waiting to send data. THIS WILL HANG IF DATA IS NOT RECEIVED
    SUCCESSFULLY; TIMEOUT SHOULD BE IMPLEMENTED AT SOME POINT"""
    host = addr[0]
    port = addr[1]

    received = 0

    while not received:
        s = socket.socket()
        s.settimeout(0.1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            s.connect(addr)
            recv_data = s.recv(1024)
            received = 1
        except:
            pass

        s.close()

    return recv_data

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
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', port))
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
