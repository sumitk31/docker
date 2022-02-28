import socket
import time
from threading import Thread

ip = "127.0.0.1"
port = 5678
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(5)
print("Server started")

def ServerThr(cls):
    print("inside Server")
    mesg = cls.recv(1024)  # convert from byte string to uni-code string
    mesg = mesg.decode("utf-8")
    time.sleep(1)
    print("MESG = ", mesg)
    cls.send(b"Hello Client")

while True:
    clientsock, clientaddr = s.accept()
    thread = Thread(target=ServerThr, args=(clientsock,))
    thread.start()


s.close()
