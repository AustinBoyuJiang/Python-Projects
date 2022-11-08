import socket
import _thread
import sys
import time


def time_now():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def send_msg(client, msg):
    client.send(msg.encode('utf8'))


def send_all(msg):
    for client in clients:
        send_msg(client, msg)


def disconnected(client, address):
    client.close()
    print("%s | The server disconnected from %s" % (time_now(), address))
    if (client in clients):
        del clients[client]


def new_client(client, address):
    if (not (address in users)):
        send_msg(client, "Welcome to the chat room with server IP: %s, give yourself a nickname:" % ip)
        try:
            users[address] = client.recv(1024).decode('utf8')
        except:
            disconnected(client, address)
            return 0
    send_all("%s | Welcome %s to the chat room" % (time_now(), users[address]))
    while (True):
        try:
            msg = client.recv(1024).decode('utf8')
            send_all("%s | %s: %s" % (time_now(), users[address], msg))
        except:
            disconnected(client, address)
            send_all("%s | %s left the chat room" % (time_now(), users[address]))
            break


if (__name__ == "__main__"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    client_maximum = 5
    server.bind((host, port))
    server.listen(client_maximum)
    clients = {}
    users = {}
    ip = socket.gethostbyname(socket.gethostname())
    print("%s | The server %s has been started and is listening for users requests..." % (time_now(), ip))
    while (True):
        client, address = server.accept()
        print("%s | The server establishes a connection with %s client" % (time_now(), address))
        clients[client] = address
        _thread.start_new_thread(new_client, (client, address,))
