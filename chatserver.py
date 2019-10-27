import socket,sys, re
from threading import Thread
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if (len(sys.argv) < 2):
    print("ENTER: python chatserver.py hostname:port")
    sys.exit()
in_list = sys.argv[1].split(':')
HOST =in_list[0]
PORT = int(in_list[1])
clients = {}
client_sockets = []
s.bind((HOST, PORT))

def accept_clients() :
    while True :
        client,client_addr = s.accept()
        print("%s:%s has connected." % client_addr)
        client.send("Hello 1 \n".encode('utf-8'))
        client_sockets.append(client)
        Thread(target= handle_client, args=(client,client_addr)).start()

def handle_client(client,client_addr) :

    n = client.recv(1024).decode('utf-8')
    name = n.strip("NICK ")
    if len(name)<=12 and re.match("^[A-Za-z0-9\_]+$",name) is not None:
        client.send("OK \n".encode('utf-8'))
    else :
        client.send(" ERROR - nickname is not valid \n".encode('utf-8'))
        name = 'unkwown'
    msg = "%s has joined the chat \n"% name
    broadcast(msg,client)
    clients[client] = name
    while True :
        message = client.recv(1024).decode('utf-8')
        msg = message.strip("MSG ")
        if not msg:
            client.close()
            del clients[client]
            snd = "%s has left the chat \n"% name
            print("%s:%s has diconnected." % client_addr)
            broadcast(snd,client)
            break
        else :
            if len(msg) > 255 and re.match("^[^\x00-\x7F]*$",msg) is None:
                client.send("ERROR - message is not valid".encode('utf-8'))
                msg_snd = "MSG "+name +" "
            else:
                msg_snd = "MSG "+name +" "+ msg
            broadcast(msg_snd,client)

def broadcast(msg, cli_conn):
    for i in client_sockets:
        if i != s and i != cli_conn :
            try:
                i.send(msg.encode('utf-8'))
            except:
                pass
i = 1
while (i == 1):
    s.listen(100)
    print("Waiting for connections")
    accept_thread = Thread(target=accept_clients)
    accept_thread.start()
    accept_thread.join()
    s.close()