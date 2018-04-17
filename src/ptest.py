import peer

host = '192.168.1.100'
port = 98765

addr = (host, port)

message = "Hi, I'm Mac."

print peer.exchange(addr, message)
