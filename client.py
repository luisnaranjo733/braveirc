#!/usr/bin/env python

''' Brave Python IRC client

# Algorithm
1. Authenticate # Implement last
2. Server goes into engine loop
3. Client queries 'online users'
4. Client queries 'recent chat'
5. Client enters chatterloop
'''

import socket
from functools import partial

import settings
from settings import HOST, logger


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(HOST)
client = settings.Communication(sock)
# Start regular communication

username = 'jnaranjo'
password = 'test'
client.Send(dict(ass=True))
