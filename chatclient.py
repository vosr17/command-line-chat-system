import socket,sys,select,string,re

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if (len(sys.argv) < 3):
    print("ENTER: python chatclient.py hostname:port nickname")
    sys.exit()
in_list = sys.argv[1].split(':')
HOST =in_list[0]
PORT = int(in_list[1])
name = sys.argv[2]
connection.settimeout(10)
connection.connect((HOST,PORT))
print(name)

while len(name)<=12 and re.match("^[A-Za-z0-9\_]+$",name) is None:
    name = raw_input("enter valid name: ")
    print(name)

nick = 'NICK '+ name
print(nick)
connection.send(nick.encode('utf-8'))
a =''
var = 1
while (var == 1) :
    socket_list = [sys.stdin,connection]
    read_list,write_list,e_list = select.select(socket_list,[], [])
    for i in read_list:
        if i == connection:
            msg_rcv = i.recv(1024).decode('utf-8')
            if not msg_rcv:
                print("Connection Lost")
                sys.exit()
            else:
                    if msg_rcv != 'MSG '+name +' '+a:
                        sys.stdout.write(msg_rcv.strip('MSG '))
                        sys.stdout.flush()
                    else :
                        continue


        else:
                a = ''
                msg = sys.stdin.readline()
                a += msg
                ms ='MSG' + msg
                connection.send(ms.encode('utf-8'))
                sys.stdout.write("You are: ")
                sys.stdout.write(msg)
                sys.stdout.flush()

connection.close()