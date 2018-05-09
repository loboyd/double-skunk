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

    send_data = convert_to_string(send_data)
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

    recv_data = convert_from_string(recv_data)
    return recv_data

def exchange(addr, send_data):
    """Exchange two pieces of data with socket connections. This function
    assumes both peers call it at approximately the same time. Otherwise,
    it will hang (should probably implement a timeout in the future)."""
    send_data = convert_to_string(send_data)

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
        # send(addr, send_data)
        if not sent:
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.settimeout(random.random()/10.)
            s.bind(('0.0.0.0', port))
            s.listen(5)
            try:
                c, _ = s.accept()
                c.send(send_data)
                c.close()
                sent = 1
            except:
                pass

    recv_data = convert_from_string(recv_data)
    return recv_data

def convert_to_string(data):
    """Convert data into a string to be sent over socket connection
    Supports strings, ints, floats, and lists of ints"""
    data_type = type(data)
    if data_type is str:
        return 's' + data
    elif data_type is int:
        return 'i' + str(data)
    elif data_type is float:
        return 'f' + str(data)
    elif data_type is list:
        return 'l' + ' '.join(map(str, data))
    else:
        raise TypeError('unsupported type')

def convert_from_string(data):
    """Convert data from socket sendable string into original data type
    Supports strings, ints, floats, and lists of ints"""
    type_flag = data[0]
    if type_flag is 's':
        return data[1:]
    elif type_flag is 'i':
        return int(data[1:])
    elif type_flag is 'f':
        return float(data[1:])
    elif type_flag is 'l':
        return map(int, data[1:].split(' '))

def get_peer_ip():
    """Get IP address of a friend. (DO SOME SANITY CHECKING HERE.)
    Eventually, nodes should publish their IP's to a server along with
    unique keys so that peer nodes can just query the server. For true
    peer-to-peer, some type of routing would need to be implemented."""
    return raw_input("Please input your friend's public IP address:\n")
