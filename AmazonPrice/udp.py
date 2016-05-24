#!/usr/bin/env python
# this is the udp broadcast server
import socket, traceback, sys, base64
host = '' # Bind to all interfaces
port = 1234

print "python UDP multi case server test"


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
ip = sys.argv[1]
port = int(sys.argv[2])
ADDR = (ip, port)
print ip,port
data = '{"cmd":"startmon","asin":"B008V8YZMM","ip":"133.130.106.179","port":2345}'
basedata = base64.b64encode(data)
s.sendto(basedata, ADDR)
