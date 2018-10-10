#!/usr/bin/env python3

import socket
import sys
import struct

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

person = input('enter your name:')
print ('hello', person)

message = input("Enter your message:")


def rawbytes(message):
	outputlist = []
	for cp in message:
		num = ord(cp)
		if num <= 255:
			outputlist.append(struct.pack('q', num))
		else:
			print("It is more than 255 characters")
	return outputlist;
rawbytes(message) 
