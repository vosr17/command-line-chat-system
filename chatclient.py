#!/usr/bin/env python3
import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
client_socket.connect((IP_address, Port))
msg = input("NICK:")

while True:
    sockets_list = [sys.stdin, client_socket]
    read_sockets,write_sockets,error_sockets= select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == client_socket:
            message = socks.recv(2048)
            print ("MSG")
        else:
            message = sys.stdin.readline()
            client_socket.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
    
