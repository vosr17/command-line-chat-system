#!/usr/bin/env python3

import socket
import sys

ip = "18.219.51.6"
port = 4711


try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("fail to connect")
	sys.exit();
print("socket created")

s.connect ((ip, port))
print("connected to ip:port")

